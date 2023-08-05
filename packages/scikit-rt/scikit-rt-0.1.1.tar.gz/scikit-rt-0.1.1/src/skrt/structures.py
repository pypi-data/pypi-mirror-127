"""Classes related to ROIs and structure sets."""

from scipy.ndimage import morphology
from shapely import geometry
import fnmatch
import matplotlib.cm
import matplotlib.colors
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pydicom
import re
import shutil
import skimage.measure

import skrt.core
import skrt.image


class ROIDefaults:
    """Singleton class for assigning default ROI names and colours."""

    # Define the single instance as a class attribute
    instance = None

    # Create single instance in inner class
    class __ROIDefaults:
        def __init__(self):

            self.n_rois = 0
            self.n_structure_sets = 0
            self.n_colors_used = 0

            self.colors = (
                list(matplotlib.cm.Set1.colors)[:-1]
                + list(matplotlib.cm.Set2.colors)[:-1]
                + list(matplotlib.cm.Set3.colors)
                + list(matplotlib.cm.tab20.colors)
            )
            for i in [9, 10]:  # Remove greys
                del self.colors[i]

    def __init__(self, reset=False):
        """Constructor of ROIDefaults singleton class."""

        if not ROIDefaults.instance:
            ROIDefaults.instance = ROIDefaults.__ROIDefaults()
        elif reset:
            ROIDefaults.instance.__init__()

    def get_default_roi_name(self):
        """Get a default name for an ROI."""

        ROIDefaults.instance.n_rois += 1
        return f"ROI {ROIDefaults.instance.n_rois}"

    def get_default_roi_color(self):
        """Get a default roi color."""

        if ROIDefaults.instance.n_colors_used >= len(ROIDefaults.instance.colors):
            return np.random.rand(3)
        color = ROIDefaults.instance.colors[ROIDefaults.instance.n_colors_used]
        ROIDefaults.instance.n_colors_used += 1
        return color

    def get_default_structure_set_name(self):
        """Get a default name for a structure set."""

        ROIDefaults.instance.n_structure_sets += 1
        return f"StructureSet {ROIDefaults.instance.n_structure_sets}"


ROIDefaults()


class ROI(skrt.image.Image):
    """Single region of interest (ROI)."""

    def __init__(
        self,
        source=None,
        name=None,
        color=None,
        load=None,
        image=None,
        shape=None,
        mask_level=0.25,
        **kwargs,
    ):

        """Load ROI from mask or contour.

        Parameters
        ----------
        source : str/array/nifti, default=None
            Source of image data to load. Can be either:
                (a) The path to a nifti file containing a binary mask;
                (b) A numpy array containing a binary mask;
                (c) The path to a file containing a numpy array;
                (d) The path to a dicom structure set file.
                (e) Dictionary of contours in the x-y orienation, where the
                keys are z positions in mm and values are lists of lists of
                3D contour points in order (x, y, z), with one list per contour
                on that slice. These contours will be used to generate a
                binary mask.

            If <source> is not given, <contours> and <shape> must be given in
            order to load an ROI directly from a contour.

        name : str, default=None
            Name of the ROI. If <source> is a file and no name is given,
            the name will be inferred from the filename.

        color : matplotlib color, default=None
            Color in which this ROI will be plotted. If None, a color
            will be assigned.

        load : bool, default=True
            If True, contours/mask will be created during initialisation;
            otherwise they will be created on-demand.

        image : Image/str, default=None
            Associated image from which to extract shape and affine matrix.

        shape : list, default=None
            Number of voxels in the image to which the ROI belongs, in
            order (x, y, z). Needed if <contours> is used instead of <source>.

        kwargs : dict, default=None
            Extra arguments to pass to the initialisation of the parent
            Image object (e.g. affine matrix if loading from a numpy array).

        """

        # Assign properties
        if isinstance(source, dict):
            self.source = None
            self.input_contours = source
        else:
            self.source = source
            self.input_contours = None
        self.custom_color = color is not None
        self.set_color(color)
        self.image = image
        if image and not isinstance(image, skrt.image.Image):
            self.image = skrt.image.Image(image)
        self.shape = shape
        self.mask_level = mask_level
        self.kwargs = kwargs

        # Create name
        self.name = name
        if self.name is None:
            if isinstance(self.source, str):
                basename = os.path.basename(self.source).split(".")[0]
                name = re.sub(r"RTSTRUCT_[MVCT]+_\d+_\d+_\d+", "", basename)
                #  self.name = name[0].upper() + name[1:]
                self.name = name
            else:
                self.name = ROIDefaults().get_default_roi_name()
        self.original_name = name

        # Load ROI data
        self.loaded = False
        self.loaded_contours = False
        self.loaded_mask = False
        if load:
            self.load()

    def clone(self, name=None):
        """Create clone of ROI, either with custom name or 'copy' appended to 
        name."""

        # Clone the ROI
        clone = Data.clone(self)

        # Set name of clone
        if name is None:
            name = self.name + " copy"
        clone.name = name
        return clone

    def load(self):
        """Load ROI from file."""

        if self.loaded:
            return

        if self.image:
            self.image.load_data()

        rois = []

        # Load from an existing Image
        if issubclass(type(self.source), skrt.image.Image):
            if not self.image:
                self.image = self.source
            skrt.image.Image.__init__(self, 
                                      self.source.get_data() > self.mask_level,
                                      affine=self.source.get_affine())
            self.loaded = True
            self.create_mask()

        # Try loading from dicom structure set
        elif isinstance(self.source, str):

            rois = load_rois_dicom(self.source, names=self.name)
            if len(rois):

                # Check a shape or image was given
                if self.shape is None and self.image is None:
                    raise RuntimeError(
                        "Must provide an associated image or "
                        "image shape if loading an ROI "
                        "from dicom!"
                    )

                # Get ROI info
                roi = rois[list(rois.keys())[0]]
                self.name = roi["name"]
                self.input_contours = roi["contours"]
                if not self.custom_color:
                    self.set_color(roi["color"])
                self.source_type = "dicom"

        # Load ROI mask
        if not self.loaded and not len(rois) and self.source is not None:
            self.source_type = "mask"
            skrt.image.Image.__init__(self, self.source, **self.kwargs)
            self.loaded = True
            self.create_mask()

        # Deal with input from dicom
        if self.input_contours is not None:

            # Create Image object
            if self.image is not None:
                self.kwargs["voxel_size"] = self.image.voxel_size
                self.kwargs["origin"] = self.image.origin
                self.shape = self.image.data.shape
                skrt.image.Image.__init__(self, np.zeros(self.shape), **self.kwargs)

            # Set x-y contours with z indices as keys
            self.contours = {"x-y": {}}
            for z, contours in self.input_contours.items():
                iz = self.image.pos_to_idx(z, "z")
                self.contours["x-y"][iz] = [
                    [tuple(p[:2]) for p in points] for points in contours
                ]
            self.loaded = True

    def get_contours(self, view="x-y"):
        """Get dict of contours in a given orientation."""

        self.create_contours()
        return self.contours[view]

    def get_mask(self, view="x-y", flatten=False):
        """Get binary mask."""

        self.load()
        self.create_mask()
        if not flatten:
            return self.data
        return np.sum(
            self.get_standardised_data(), axis=skrt.image._slice_axes[view]
        ).astype(bool)

    def get_polygons(self, view="x-y", sl=None, idx=None, pos=None):
        """Get shapely polygon objects corresponding to a given slice."""

        if sl is None and idx is None and pos is None:
            idx = self.get_mid_idx(view)
        else:
            idx = self.get_idx(view, sl, idx, pos)

        if not hasattr(self, "contours") or view not in self.contours:
            self.create_contours()
        if idx not in self.contours[view]:
            print("Warning: No contour found at index:", idx)
            return []

        return [geometry.Polygon(p) for p in self.contours[view][idx]]

    def create_contours(self, force=False):
        """Create contours in all orientations."""

        if self.loaded_contours and not force:
            return
        if not self.loaded:
            self.load()

        self.create_mask()
        if not hasattr(self, "contours") or force:
            self.contours = {}

        # Create contours in every orientation
        for view, z_ax in skrt.image._slice_axes.items():
            if view in self.contours:
                continue

            # Make new contours from mask
            self.contours[view] = {}
            for iz in range(self.n_voxels[z_ax]):

                # Get slice of mask array
                mask_slice = self.get_slice(view, idx=iz).T
                if mask_slice.max() < 0.5:
                    continue

                points = self.mask_to_contours(mask_slice, view)
                if points:
                    self.contours[view][iz] = points

        self.loaded_contours = True

    def mask_to_contours(self, mask, view, invert=False):
        """Create contours from a mask."""

        contours = skimage.measure.find_contours(mask, 0.5, "low", "low")

        # Convert indices to positions in mm
        x_ax, y_ax = skrt.image._plot_axes[view]
        points = []
        for contour in contours:
            contour_points = []
            for ix, iy in contour:
                px = self.idx_to_pos(ix, x_ax)
                py = self.idx_to_pos(iy, y_ax)
                if invert:
                    px, py = py, px
                contour_points.append((px, py))
            points.append(contour_points)

        return points

    def create_mask(self):
        """Create binary mask."""

        if self.loaded_mask:
            return
        if not self.loaded:
            self.load()

        # Create mask from x-y contours if needed
        if self.input_contours:

            # Check an image or shape was given
            if self.image is None and self.shape is None:
                raise RuntimeError(
                    "Must set ROI.image or ROI.shape"
                    " before creating mask!"
                )
            if self.image is None:
                skrt.image.Image.__init__(self, np.zeros(self.shape), **self.kwargs)

            # Create mask on each z layer
            for z, contours in self.input_contours.items():

                # Convert z position to index
                iz = self.pos_to_idx(z, "z")

                # Loop over each contour on the z slice
                pos_to_idx_vec = np.vectorize(self.pos_to_idx)
                for points in contours:

                    # Convert (x, y) positions to array indices
                    points_idx = np.zeros((points.shape[0], 2))
                    for i in range(2):
                        points_idx[:, i] = pos_to_idx_vec(
                            points[:, i], i, return_int=False
                        )

                    # Create polygon
                    polygon = geometry.Polygon(points_idx)

                    # Get polygon's bounding box
                    ix1, iy1, ix2, iy2 = [int(xy) for xy in polygon.bounds]
                    ix1 = max(0, ix1)
                    ix2 = min(ix2 + 1, self.shape[1])
                    iy1 = max(0, iy1)
                    iy2 = min(iy2 + 1, self.shape[0])

                    # Loop over pixels
                    for ix in range(ix1, ix2):
                        for iy in range(iy1, iy2):

                            # Make polygon of current pixel
                            pixel = geometry.Polygon(
                                [
                                    [ix - 0.5, iy - 0.5],
                                    [ix - 0.5, iy + 0.5],
                                    [ix + 0.5, iy + 0.5],
                                    [ix + 0.5, iy - 0.5],
                                ]
                            )

                            # Compute overlap
                            overlap = polygon.intersection(pixel).area
                            self.data[iy, ix, int(iz)] += overlap

            self.data = self.data > self.mask_level

        # Convert to boolean mask
        if hasattr(self, "data"):
            if not self.data.dtype == "bool":
                self.data = self.data > self.mask_level
            if not hasattr(self, "empty"):
                self.empty = not np.any(self.data)
            self.loaded_mask = True

    def resample(self, *args, **kwargs):
        self.create_mask()
        skrt.image.Image.resample(self, *args, **kwargs)

    def match_voxel_size(self, other, *args, **kwargs):

        if isinstance(other, ROI):
            other.create_mask()
        self.create_mask()
        skrt.image.Image.match_voxel_size(self, other, *args, **kwargs)

    def get_slice(self, *args, **kwargs):

        self.create_mask()
        return skrt.image.Image.get_slice(self, *args, **kwargs).astype(bool)

    def get_indices(self, view="x-y", slice_num=False):
        """Get list of slice indices on which this ROI exists. If
        <slice_num> is True, slice numbers will be returned instead of
        indices."""

        if not hasattr(self, "contours") or view not in self.contours:
            self.create_contours()
        indices = list(self.contours[view].keys())
        if slice_num:
            z_ax = skrt.image._slice_axes[view]
            return [self.idx_to_slice(i, z_ax) for i in indices]
        else:
            return indices

    def get_mid_idx(self, view="x-y", slice_num=False):
        """Get central slice index of this ROI in a given orientation."""

        indices = self.get_indices(view, slice_num=slice_num)
        if not len(indices):
            return None
        return round(np.mean(indices))

    def on_slice(self, view, sl=None, idx=None, pos=None):
        """Check whether this ROI exists on a given slice."""

        idx = self.get_idx(view, sl, idx, pos)
        if hasattr(self, 'contours') and view in self.contours:
            return idx in self.contours[view]
        else:
            self.create_mask()
            return idx in self.get_indices(view)

    def get_centroid(
        self,
        view=None,
        sl=None,
        idx=None,
        pos=None,
        units="mm",
        standardise=True,
        flatten=False,
    ):
        """Get centroid position in 2D or 3D."""

        # Get 2D or 3D data from which to calculate centroid
        if view or sl or idx or pos:
            if sl is None and idx is None and pos is None:
                idx = self.get_mid_idx(view)
            if view is None:
                view = "x-y"
            if not self.on_slice(view, sl, idx, pos):
                return [None, None]
            data = self.get_slice(view, sl, idx, pos)
            axes = skrt.image._plot_axes[view]
        else:
            if flatten:
                if view is None:
                    view = "x-y"
                data = self.get_mask(view, flatten=True)
            else:
                self.create_mask()
                data = self.get_data(standardise)
            axes = skrt.image._axes

        # Compute centroid
        non_zero = np.argwhere(data)
        if not len(non_zero):
            if data.ndim == 2:
                return None, None
            else:
                return None, None, None
        centroid_rowcol = list(non_zero.mean(0))
        centroid = [centroid_rowcol[1], centroid_rowcol[0]] + centroid_rowcol[2:]

        # Convert to mm
        if units == "mm":
            centroid = [self.idx_to_pos(c, axes[i]) for i, c in enumerate(centroid)]
        return centroid

    def get_centre(
        self, view=None, sl=None, idx=None, pos=None, units="mm", standardise=True
    ):
        """Get centre position in 2D or 3D."""

        # Get 2D or 3D data for which to calculate centre
        if view is None:
            data = self.get_data(standardise)
            axes = skrt.image._axes
        else:
            if sl is None and idx is None and pos is None:
                idx = self.get_mid_idx(view)
            data = self.get_slice(view, sl, idx, pos)
            axes = skrt.image._plot_axes[view]

        # Calculate mean of min and max positions
        non_zero = np.argwhere(data)
        if not len(non_zero):
            return [0 for i in axes]
        centre_rowcol = list((non_zero.max(0) + non_zero.min(0)) / 2)
        centre = [centre_rowcol[1], centre_rowcol[0]] + centre_rowcol[2:]

        # Convert to mm
        if units == "mm":
            centre = [self.idx_to_pos(c, axes[i]) for i, c in enumerate(centre)]
        return centre

    def get_volume(self, units="mm"):
        """Get ROI volume."""

        if hasattr(self, "volume"):
            return self.volume[units]

        self.create_mask()
        self.volume = {}
        self.volume["voxels"] = self.data.astype(bool).sum()
        self.volume["mm"] = self.volume["voxels"] * abs(np.prod(self.voxel_size))
        self.volume["ml"] = self.volume["mm"] * (0.1 ** 3)
        return self.volume[units]

    def get_area(
        self, view="x-y", sl=None, idx=None, pos=None, units="mm", flatten=False
    ):
        """Get the area of the ROI on a given slice."""

        if view is None:
            view = "x-y"
        if sl is None and idx is None and pos is None:
            idx = self.get_mid_idx(view)
        im_slice = self.get_slice(view, sl, idx, pos, flatten=flatten)
        area = im_slice.astype(bool).sum()
        if units == "mm":
            x_ax, y_ax = skrt.image._plot_axes[view]
            area *= abs(self.voxel_size[x_ax] * self.voxel_size[y_ax])
        return area

    def get_length(self, units="mm", ax="z"):
        """Get total length of the ROI along a given axis."""

        if hasattr(self, "length") and ax in self.length:
            return self.length[ax][units]

        self.create_mask()
        if not hasattr(self, "length"):
            self.length = {}
        self.length[ax] = {}

        nonzero = np.argwhere(self.data)
        vals = nonzero[:, skrt.image._axes.index(ax)]
        if len(vals):
            self.length[ax]["voxels"] = max(vals) + 1 - min(vals)
            self.length[ax]["mm"] = self.length[ax]["voxels"] * abs(
                self.voxel_size[skrt.image._axes.index(ax)]
            )
        else:
            self.length[ax] = {"voxels": 0, "mm": 0}

        return self.length[ax][units]

    def get_geometry(
        self,
        metrics=["volume", "area", "centroid", "x_length", "y_length", "z_length"],
        vol_units="mm",
        area_units="mm",
        length_units="mm",
        centroid_units="mm",
        view=None,
        sl=None,
        pos=None,
        idx=None,
    ):
        """Get a pandas DataFrame of the geometric properties listed in
        <metrics>.

        Possible metrics:
            - 'volume': volume of entire ROI.
            - 'area': area either of the central x-y slice, or of a given
            view/slice if either sl/pos/idx are given.
            - 'centroid': centre-of-mass either of the entire ROI, or a
            given view/slice if either sl/pos/idx are given.
            - 'centroid_global': centre-of-mass of the entire ROI (note
            that this is the same as 'centroid' if sl/pos/idx are all None)
            - 'x_length': ROI length along the x axis
            - 'y_length': ROI length along the y axis
            - 'z_length': ROI length along the z axis
        """

        # Parse volume and area units
        vol_units_name = vol_units
        if vol_units in ["mm", "mm3"]:
            vol_units = "mm"
            vol_units_name = "mm3"
        area_units_name = vol_units
        if area_units in ["mm", "mm2"]:
            area_units = "mm"
            area_units_name = "mm2"

        # Make dict of property names
        names = {
            "volume": f"Volume ({vol_units_name})",
            "area": f"Area ({area_units_name})",
        }
        for ax in skrt.image._axes:
            names[f"{ax}_length"] = f"{ax} length ({length_units})"
            names[f"centroid_{ax}"] = f"Centroid {ax} ({centroid_units})"
            names[f"centroid_global_{ax}"] = f"Global centroid {ax} ({centroid_units})"

        # Make dict of functions and args for each metric
        funcs = {
            "volume": (self.get_volume, {"units": vol_units}),
            "area": (
                self.get_area,
                {"units": area_units, "view": view, "sl": sl, "pos": pos, "idx": idx},
            ),
            "centroid": (
                self.get_centroid,
                {
                    "units": centroid_units,
                    "view": view,
                    "sl": sl,
                    "pos": pos,
                    "idx": idx,
                },
            ),
            "centroid_global": (self.get_centroid, {"units": centroid_units}),
        }
        for ax in skrt.image._axes:
            funcs[f"{ax}_length"] = (self.get_length, {"ax": ax, "units": length_units})

        # Make dict of metrics
        geom = {m: funcs[m][0](**funcs[m][1]) for m in metrics}

        # Split centroid into multiple entries
        for cname in ["centroid", "centroid_global"]:
            if cname in geom:
                centroid_vals = geom.pop(cname)
                axes = (
                    [0, 1, 2]
                    if len(centroid_vals) == 3
                    else skrt.image._plot_axes[view]
                )
                for i, i_ax in enumerate(axes):
                    ax = skrt.image._axes[i_ax]
                    geom[f"{cname}_{ax}"] = centroid_vals[i]

        geom_named = {names[m]: g for m, g in geom.items()}
        return pd.DataFrame(geom_named, index=[self.name])

    def get_centroid_vector(self, roi, **kwargs):
        """Get centroid displacement vector with respect to another ROI."""

        this_centroid = np.array(self.get_centroid(**kwargs))
        other_centroid = np.array(roi.get_centroid(**kwargs))
        if None in this_centroid or None in other_centroid:
            return None, None
        return other_centroid - this_centroid

    def get_centroid_distance(self, roi, **kwargs):
        """Get absolute centroid distance."""

        centroid = self.get_centroid_vector(roi, **kwargs)
        if None in centroid:
            return None
        return np.linalg.norm(centroid)

    def get_dice(self, roi, view="x-y", sl=None, idx=None, pos=None, flatten=False):
        """Get Dice score, either global or on a given slice."""

        if view is None:
            view = "x-y"
        if sl is None and idx is None and pos is None:
            data1 = self.get_mask(view, flatten)
            data2 = roi.get_mask(view, flatten)
        else:
            data1 = self.get_slice(view, sl, idx, pos)
            data2 = roi.get_slice(view, sl, idx, pos)

        return (data1 & data2).sum() / np.mean([data1.sum(), data2.sum()])

    def get_volume_ratio(self, roi):
        """Get ratio of another ROI's volume with respect to own volume."""

        own_volume = roi.get_volume()
        other_volume = self.get_volume()
        if not other_volume:
            return None
        return own_volume / other_volume

    def get_area_ratio(self, roi, **kwargs):
        """Get ratio of another ROI's area with respect to own area."""

        own_area = roi.get_area(**kwargs)
        other_area = self.get_area(**kwargs)
        if not other_area:
            return None
        return own_area / other_area

    def get_relative_volume_diff(self, roi, units="mm"):
        """Get relative volume of another ROI with respect to own volume."""

        own_volume = self.get_volume(units)
        other_volume = roi.get_volume(units)
        if not own_volume:
            return None
        return (own_volume - other_volume) / own_volume

    def get_area_diff(self, roi, **kwargs):
        """Get absolute area difference between two ROIs."""

        own_area = self.get_area(**kwargs)
        other_area = roi.get_area(**kwargs)
        if not own_area or not other_area:
            return None
        return own_area - other_area

    def get_relative_area_diff(self, roi, **kwargs):
        """Get relative area of another ROI with respect to own area."""

        own_area = self.get_area(**kwargs)
        other_area = roi.get_area(**kwargs)
        if not own_area or not other_area:
            return None
        return (own_area - other_area) / own_area

    def get_surface_distances(
        self,
        roi,
        signed=False,
        view=None,
        sl=None,
        idx=None,
        pos=None,
        connectivity=2,
        flatten=False,
    ):
        """Get vector of surface distances between two ROIs."""

        # Ensure both ROIs are loaded
        self.load()
        roi.load()

        # Check whether ROIs are empty
        if not np.any(self.get_mask()) or not np.any(roi.get_mask()):
            return

        # Get binary masks and voxel sizes
        if flatten and view is None:
            view = "x-y"
        if view or sl or idx or pos:
            voxel_size = [self.voxel_size[i] for i in skrt.image._plot_axes[view]]
            if not flatten:
                mask1 = self.get_slice(view, sl=sl, idx=idx, pos=pos)
                mask2 = roi.get_slice(view, sl=sl, idx=idx, pos=pos)
            else:
                mask1 = self.get_mask(view, True)
                mask2 = roi.get_mask(view, True)
        else:
            vx, vy, vz = self.voxel_size
            voxel_size = [vy, vx, vz]
            mask1 = self.get_mask()
            mask2 = roi.get_mask()

        # Make structuring element
        conn2 = morphology.generate_binary_structure(2, connectivity)
        if mask1.ndim == 2:
            conn = conn2
        else:
            conn = np.zeros((3, 3, 3), dtype=bool)
            conn[:, :, 1] = conn2

        # Get outer pixel of binary maps
        surf1 = mask1 ^ morphology.binary_erosion(mask1, conn)
        surf2 = mask2 ^ morphology.binary_erosion(mask2, conn)

        # Make arrays of distances to surface of each pixel
        dist1 = morphology.distance_transform_edt(~surf1, voxel_size)
        dist2 = morphology.distance_transform_edt(~surf2, voxel_size)

        # Get signed arrays
        if signed:
            dist1 = dist1 * ~mask1 - dist1 * mask1
            dist2 = dist2 * ~mask2 - dist2 * mask2

        # Make vector containing all distances
        sds = np.concatenate([np.ravel(dist1[surf2 != 0]), np.ravel(dist2[surf1 != 0])])
        return sds

    def get_mean_surface_distance(self, roi, **kwargs):

        sds = self.get_surface_distances(roi, **kwargs)
        if sds is None:
            return
        return sds.mean()

    def get_rms_surface_distance(self, roi, **kwargs):

        sds = self.get_surface_distances(roi, **kwargs)
        if sds is None:
            return
        return np.sqrt((sds ** 2).mean())

    def get_hausdorff_distance(self, roi, **kwargs):

        sds = self.get_surface_distances(roi, **kwargs)
        if sds is None:
            return
        return sds.max()

    def get_surface_distance_metrics(self, roi, **kwargs):
        """Get the mean surface distance, RMS surface distance, and Hausdorff
        distance."""

        sds = self.get_surface_distances(roi, **kwargs)
        if sds is None:
            return
        return sds.mean(), np.sqrt((sds ** 2).mean()), sds.max()

    def plot_surface_distances(self, roi, save_as=None, signed=False, **kwargs):
        """Plot histogram of surface distances."""

        sds = self.get_surface_distances(roi, signed=signed, **kwargs)
        if sds is None:
            return
        fig, ax = plt.subplots()
        ax.hist(sds)
        xlabel = (
            "Surface distance (mm)" if not signed else "Signed surface distance (mm)"
        )
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Number of voxels")
        if save_as:
            plt.tight_layout()
            fig.savefig(save_as)

    def get_comparison(
        self,
        roi,
        metrics=["dice", "abs_centroid", "rel_volume_diff", "rel_area_diff"],
        fancy_names=True,
        vol_units="mm",
        area_units="mm",
        centroid_units="mm",
        view=None,
        sl=None,
        idx=None,
        pos=None,
    ):
        """Get a pandas DataFrame of comparison metrics with another ROI.

        Possible metrics:
            - 'dice': Dice score, either on a slice (if view and sl/idx/pos
            are given), or globally.
            - 'dice_global': Global dice score (note that this is the same as
            'dice' if no view and sl/idx/pos are given).
            - 'dice_flat': Global dice score of flat ROIs.
            - 'centroid_global': Centroid distance vector.
            - 'abs_centroid_global': Absolute centroid distance.
            - 'centroid': Centroid distance vector on slice.
            - 'abs_centroid': Absolute centroid distance on slice.
            - 'abs_centroid_flat': Absolute centroid distance on flat ROIs.
            - 'rel_volume_diff': Relative volume difference.
            - 'area_diff': Absolute area difference.
            - 'area_diff_flat': Absolute area difference of projections of
            each ROI.
            - 'rel_area_diff': Relative area difference, either on a specific
            slice or on the central 'x-y' slice of each ROI, if no
            view and idx/pos/sl are given.
            - 'rel_area_diff_flat': Relative area difference of projections of
            each ROI.
            - 'volume_ratio': Volume ratio.
            - 'area_ratio': Area ratio, either on a specific slice or of the
            central slices of the two ROIs.
            - 'area_ratio_flat': Area ratio of projections of each ROI.
            - 'mean_surface_distance': Mean surface distance.
            - 'mean_surface_distance_flat': Mean surface distance of
            flat ROIs.
            - 'mean_surface_distance_signed_flat': Mean signed surface
            distance of flat ROIs.
            - 'rms_surface_distance'
            - 'rms_surface_distance_flat'
            - 'hausdorff_distance'
            - 'hausdorff_distance_flat'

        """

        # Parse volume and area units
        vol_units_name = vol_units
        if vol_units in ["mm", "mm3"]:
            vol_units = "mm"
            vol_units_name = "mm3"
        area_units_name = vol_units
        if area_units in ["mm", "mm2"]:
            area_units = "mm"
            area_units_name = "mm2"

        # Make dict of property names
        names = {
            "dice": "Dice score",
            "dice_global": "Global Dice score",
            "dice_flat": "Flattened Dice score",
            "abs_centroid": f"Centroid distance ({centroid_units})",
            "abs_centroid_flat": f"Flattened centroid distance ({centroid_units})",
            "abs_centroid_global": f"Global centroid distance ({centroid_units})",
            "rel_volume_diff": f"Relative volume difference ({vol_units_name})",
            "area_diff": f"Area difference ({area_units_name})",
            "area_diff_flat": f"Flattened area difference ({area_units_name})",
            "rel_area_diff": f"Relative area difference ({area_units_name})",
            "rel_area_diff_flat": f"Flattened relative area difference ({area_units_name})",
            "volume_ratio": "Volume ratio",
            "area_ratio": "Area ratio",
            "area_ratio_flat": "Flattened area ratio",
            "mean_surface_distance": "Mean surface distance (mm)",
            "mean_surface_distance_flat": "Flattened mean surface distance (mm)",
            "mean_surface_distance_signed_flat": "Flattened mean signed surface distance (mm)",
            "rms_surface_distance": "RMS surface distance (mm)",
            "rms_surface_distance_flat": "Flattened RMS surface distance (mm)",
            "hausdorff_distance": "Hausdorff distance (mm)",
            "hausdorff_distance_flat": "Flattened Hausdorff distance (mm)",
        }
        for ax in skrt.image._axes:
            names[f"centroid_{ax}"] = f"Centroid {ax} distance ({centroid_units})"
            names[
                f"centroid_global_{ax}"
            ] = f"Global centroid {ax} distance ({centroid_units})"

        # Make dict of functions and args for each metric
        funcs = {
            "dice": (
                self.get_dice,
                {"roi": roi, "view": view, "sl": sl, "idx": idx, "pos": pos},
            ),
            "dice_global": (self.get_dice, {"roi": roi}),
            "dice_flat": (self.get_dice, {"roi": roi, "flatten": True}),
            "abs_centroid": (
                self.get_centroid_distance,
                {
                    "roi": roi,
                    "units": centroid_units,
                    "view": view,
                    "sl": sl,
                    "pos": pos,
                    "idx": idx,
                },
            ),
            "abs_centroid_flat": (
                self.get_centroid_distance,
                {
                    "roi": roi,
                    "flatten": True,
                    "units": centroid_units,
                    "view": view,
                    "sl": sl,
                    "pos": pos,
                    "idx": idx,
                },
            ),
            "centroid": (
                self.get_centroid_vector,
                {
                    "roi": roi,
                    "units": centroid_units,
                    "view": view,
                    "sl": sl,
                    "pos": pos,
                    "idx": idx,
                },
            ),
            "abs_centroid_global": (
                self.get_centroid_distance,
                {"roi": roi, "units": centroid_units},
            ),
            "centroid_global": (
                self.get_centroid_vector,
                {"roi": roi, "units": centroid_units},
            ),
            "rel_volume_diff": (
                self.get_relative_volume_diff,
                {"roi": roi, "units": vol_units},
            ),
            "rel_area_diff": (
                self.get_relative_area_diff,
                {
                    "roi": roi,
                    "units": area_units,
                    "view": view,
                    "sl": sl,
                    "pos": pos,
                    "idx": idx,
                },
            ),
            "rel_area_diff_flat": (
                self.get_relative_area_diff,
                {"roi": roi, "units": area_units, "flatten": True},
            ),
            "volume_ratio": (self.get_volume_ratio, {"roi": roi}),
            "area_ratio": (
                self.get_area_ratio,
                {"roi": roi, "view": view, "sl": sl, "pos": pos, "idx": idx},
            ),
            "area_ratio_flat": (self.get_area_ratio, {"roi": roi, "flatten": True}),
            "area_diff": (
                self.get_area_diff,
                {"roi": roi, "view": view, "sl": sl, "pos": pos, "idx": idx},
            ),
            "area_diff_flat": (self.get_area_diff, {"roi": roi, "flatten": True}),
            "mean_surface_distance": (self.get_mean_surface_distance, {"roi": roi},),
            "mean_surface_distance_flat": (
                self.get_mean_surface_distance,
                {"roi": roi, "flatten": True},
            ),
            "mean_surface_distance_signed_flat": (
                self.get_mean_surface_distance,
                {"roi": roi, "flatten": True, "signed": True},
            ),
            "rms_surface_distance": (self.get_rms_surface_distance, {"roi": roi},),
            "rms_surface_distance_flat": (
                self.get_rms_surface_distance,
                {"roi": roi, "flatten": True},
            ),
            "hausdorff_distance": (self.get_hausdorff_distance, {"roi": roi},),
            "hausdorff_distance_flat": (
                self.get_hausdorff_distance,
                {"roi": roi, "flatten": True},
            ),
        }

        # Make dict of metrics
        comp = {m: funcs[m][0](**funcs[m][1]) for m in metrics}

        # Split centroid into multiple entries
        for cname in ["centroid", "centroid_global"]:
            if cname in comp:
                centroid_vals = comp.pop(cname)
                if view is None:
                    view = "x-y"
                axes = (
                    [0, 1, 2]
                    if len(centroid_vals) == 3
                    else skrt.image._plot_axes[view]
                )
                for i, i_ax in enumerate(axes):
                    ax = skrt.image._axes[i_ax]
                    comp[f"{cname}_{ax}"] = centroid_vals[i]

        if fancy_names:
            comp = {names[m]: c for m, c in comp.items()}
        name = self.get_comparison_name(roi)
        return pd.DataFrame(comp, index=[name])

    def get_comparison_name(self, roi, camelcase=False):
        """Get name of comparison between this ROI and another."""

        if self.name == roi.name:
            name = self.name
            if camelcase:
                return name.replace(" ", "_")
            return name
        else:
            if camelcase:
                return f"{self.name}_vs_{roi.name}".replace(" ", "_")
            return f"{self.name} vs. {roi.name}"

    def set_color(self, color):
        """Set plotting color."""

        if color is not None and not matplotlib.colors.is_color_like(color):
            print(f"Warning: {color} not a valid color!")
            color = None
        if color is None:
            color = ROIDefaults().get_default_roi_color()
        self.color = matplotlib.colors.to_rgba(color)

    def plot(
        self,
        view="x-y",
        plot_type="contour",
        sl=None,
        idx=None,
        pos=None,
        opacity=None,
        linewidth=None,
        contour_kwargs=None,
        mask_kwargs=None,
        zoom=None,
        zoom_centre=None,
        color=None,
        **kwargs,
    ):
        """Plot this ROI as either a mask or a contour."""

        show_centroid = "centroid" in plot_type
        if zoom and zoom_centre is None:
            zoom_centre = self.get_zoom_centre(view)
        if color is None:
            color = self.color

        # Plot a mask
        if plot_type == "mask":
            self.plot_mask(
                view,
                sl,
                idx,
                pos,
                mask_kwargs,
                opacity,
                zoom_centre=zoom_centre,
                **kwargs,
            )

        # Plot a contour
        elif plot_type in ["contour", "centroid"]:
            self.plot_contour(
                view,
                sl,
                idx,
                pos,
                contour_kwargs,
                linewidth,
                centroid=show_centroid,
                zoom=zoom,
                zoom_centre=zoom_centre,
                color=color,
                **kwargs,
            )

        # Plot transparent mask + contour
        elif "filled" in plot_type:
            if opacity is None:
                opacity = 0.3
            self.plot_mask(view, sl, idx, pos, mask_kwargs, opacity, **kwargs)
            kwargs["ax"] = self.ax
            kwargs["include_image"] = False
            self.plot_contour(
                view,
                sl,
                idx,
                pos,
                contour_kwargs,
                linewidth,
                centroid=show_centroid,
                zoom=zoom,
                zoom_centre=zoom_centre,
                color=color,
                **kwargs,
            )

        else:
            print("Unrecognised ROI plotting option:", plot_type)

    def plot_mask(
        self,
        view="x-y",
        sl=None,
        idx=None,
        pos=None,
        mask_kwargs=None,
        opacity=None,
        ax=None,
        gs=None,
        figsize=skrt.image._default_figsize,
        include_image=False,
        zoom=None,
        zoom_centre=None,
        color=None,
        flatten=False,
        show=True,
        **kwargs,
    ):
        """Plot the ROI as a mask."""

        if sl is None and idx is None and pos is None:
            idx = self.get_mid_idx(view)
        else:
            idx = self.get_idx(view, sl, idx, pos)
        self.create_mask()
        self.set_ax(view, ax, gs, figsize)
        mask_slice = self.get_slice(view, idx=idx, flatten=flatten)

        # Make colormap
        norm = matplotlib.colors.Normalize()
        cmap = matplotlib.cm.hsv
        s_colors = cmap(norm(mask_slice))
        if color is None:
            color = self.color
        s_colors[mask_slice > 0, :] = color
        s_colors[mask_slice == 0, :] = (0, 0, 0, 0)

        # Get plotting arguments
        if mask_kwargs is None:
            mask_kwargs = {}
        mask_kwargs.setdefault("alpha", opacity)
        mask_kwargs.setdefault("interpolation", "none")

        # Make plot
        if include_image:
            self.image.plot(view, idx=idx, ax=self.ax, show=False)
        self.ax.imshow(s_colors, extent=self.plot_extent[view], **mask_kwargs)

        # Adjust axes
        self.label_ax(view, idx, **kwargs)
        self.zoom_ax(view, zoom, zoom_centre)
        if show:
            plt.show()

    def plot_contour(
        self,
        view="x-y",
        sl=None,
        idx=None,
        pos=None,
        contour_kwargs=None,
        linewidth=None,
        centroid=False,
        ax=None,
        gs=None,
        figsize=None,
        include_image=False,
        zoom=None,
        zoom_centre=None,
        color=None,
        flatten=False,
        show=True,
        **kwargs,
    ):
        """Plot the ROI as a contour."""

        self.load()
        if not hasattr(self, "contours") or view not in self.contours:
            self.create_contours()

        if sl is None and idx is None and pos is None:
            idx = self.get_mid_idx(view)
        else:
            idx = self.get_idx(view, sl, idx, pos)
        if not self.on_slice(view, idx=idx):
            return
        if figsize is None:
            x_ax, y_ax = skrt.image._plot_axes[view]
            aspect = self.get_length(ax=skrt.image._axes[x_ax]) / self.get_length(
                ax=skrt.image._axes[y_ax]
            )
            figsize = (
                aspect * skrt.image._default_figsize,
                skrt.image._default_figsize,
            )
        self.set_ax(view, ax, gs, figsize)

        contour_kwargs = {} if contour_kwargs is None else contour_kwargs
        contour_kwargs.setdefault("color", color)
        contour_kwargs.setdefault("linewidth", linewidth)

        # Plot underlying image
        if include_image:
            self.image.plot(view, idx=idx, ax=self.ax, show=False)

        # Get contour points
        if flatten:
            mask = self.get_slice(view, idx=idx, flatten=True)
            contours = self.mask_to_contours(mask, view, invert=True)
        else:
            contours = self.contours[view][idx]

        # Plot contour
        for points in contours:
            points_x = [p[0] for p in points]
            points_y = [p[1] for p in points]
            points_x.append(points_x[0])
            points_y.append(points_y[0])
            self.ax.plot(points_x, points_y, **contour_kwargs)

        # Check whether y axis needs to be inverted
        if not (self.plot_extent[view][3] > self.plot_extent[view][2]) == (
            self.ax.get_ylim()[1] > self.ax.get_ylim()[0]
        ):
            self.ax.invert_yaxis()

        # Plot centroid point
        if centroid:
            self.ax.plot(
                *self.get_centroid(view, sl, idx, pos, flatten=flatten),
                "+",
                **contour_kwargs,
            )

        # Adjust axes
        self.ax.set_aspect("equal")
        self.label_ax(view, idx, **kwargs)
        self.zoom_ax(view, zoom, zoom_centre)
        if show:
            plt.show()

    def plot_comparison(self, other, legend=True, save_as=None, names=None, 
                        show=True, **kwargs):
        """Plot comparison with another ROI."""

        if self.color == other.color:
            roi2_color = ROIDefaults().get_default_roi_color()
        else:
            roi2_color = other.color

        self.plot(show=False, **kwargs)
        if kwargs is None:
            kwargs = {}
        else:
            kwargs = kwargs.copy()
        kwargs["ax"] = self.ax
        kwargs["color"] = roi2_color
        kwargs["include_image"] = False
        other.plot(show=False, **kwargs)
        self.ax.set_title(self.get_comparison_name(other))

        if legend:
            if names:
                roi1_name = names[0]
                roi2_name = names[1]
            else:
                roi1_name = self.name
                roi2_name = other.name
            handles = [
                mpatches.Patch(color=self.color, label=roi1_name),
                mpatches.Patch(color=roi2_color, label=roi2_name),
            ]
            self.ax.legend(
                handles=handles, framealpha=1, facecolor="white", 
                loc="lower left"
            )

        if show:
            plt.show()

        if save_as:
            plt.tight_layout()
            self.fig.savefig(save_as)

    def get_zoom_centre(self, view):
        """Get coordinates to zoom in on this ROI."""

        zoom_centre = [None, None, None]
        x_ax, y_ax = skrt.image._plot_axes[view]
        x, y = self.get_centre(view)
        zoom_centre[x_ax] = x
        zoom_centre[y_ax] = y
        return zoom_centre

    def view(self, **kwargs):

        from skrt.viewer import QuickViewer

        self.load()

        # Create image to view
        if self.image:
            im_source = '.tmp_image.nii.gz'
            self.image.write(im_source)
        else:
            im_source = np.zeros(self.get_mask().shape)

        # Save to temp file
        if isinstance(self.source, str):
            roi_source = self.source
        else:
            roi_source = ".tmp_rois.nii.gz"
            self.write(roi_source)

        QuickViewer(im_source, affine=self.get_affine(), title=self.name, 
                    structs=roi_source, struct_names={self.name: "*"}, 
                    **kwargs)

        os.remove(im_source)
        os.remove(roi_source)

    def write(self, outname=None, outdir=".", ext=None, **kwargs):

        self.load()

        # Generate output name if not given
        possible_ext = [".dcm", ".nii.gz", ".nii", ".npy", ".txt"]
        if outname is None:
            if ext is None:
                ext = ".nii"
            else:
                if ext not in possible_ext:
                    raise RuntimeError(f"Unrecognised file extension: {ext}")
            if not ext.startswith("."):
                ext = f".{ext}"
            outname = f"{outdir}/{self.name}{ext}"

        # Otherwise, infer extension from filename
        else:

            # Find any of the valid file extensions
            for pos in possible_ext:
                if outname.endswith(pos):
                    ext = pos
            if ext not in possible_ext:
                raise RuntimeError(f"Unrecognised output file type: {outname}")

            outname = os.path.join(outdir, outname)

        # Write points to text file
        if ext == ".txt":

            self.load()
            if "x-y" not in self.contours:
                self.create_contours()

            with open(outname, "w") as file:
                file.write("point\n")
                points = []
                for z, contours in self.contours["x-y"].items():
                    for contour in contours:
                        for point in contour:
                            points.append(f"{point[0]} {point[1]} {z}")
                file.write(str(len(points)) + "\n")
                file.write("\n".join(points))
                file.close()
            return

        # Write array to nifti or npy
        elif ext != ".dcm":
            self.create_mask()
            skrt.image.Image.write(self, outname, **kwargs)
        else:
            print("Warning: dicom ROI writing not currently available!")

    def transform(self, **kwargs):
        """Transform mask and ensure that contours will be remade."""

        self.create_mask()
        cx, cy, _ = self.get_centroid()
        skrt.image.Image.transform(self, centre=(cx, cy), **kwargs)

        if self.loaded_contours:
            self.loaded_contours = False
            delattr(self, "contours")
            self.input_contours = None


class StructureSet(skrt.core.Archive):
    """Structure set."""

    def __init__(
        self,
        sources=None,
        name=None,
        image=None,
        load=True,
        names=None,
        to_keep=None,
        to_remove=None,
        multi_label=False
    ):
        """Load structure set from source(s)."""

        self.name = name
        if name is None:
            self.name = ROIDefaults().get_default_structure_set_name()
        self.sources = sources
        if self.sources is None:
            self.sources = []
        elif not skrt.core.is_list(sources):
            self.sources = [sources]
        self.rois = []
        self.set_image(image)
        self.to_keep = to_keep
        self.to_remove = to_remove
        self.names = names
        self.multi_label = multi_label

        path = sources if isinstance(sources, str) else ""
        skrt.core.Archive.__init__(self, path)

        self.loaded = False
        if load:
            self.load()

    def __getitem__(self, roi):
        if isinstance(roi, int):
            return self.get_rois()[roi]
        elif isinstance(roi, str):
            return self.get_roi_dict()[roi]

    def __iter__(self):
        return StructureSetIterator(self)

    def load(self, sources=None, force=False):
        """Load structure set from source(s). If None, will load from own
        self.sources."""

        if self.loaded and not force and sources is None:
            return

        if sources is None:
            sources = self.sources

        if self.multi_label and isinstance(sources, np.ndarray):

            n = sources.max()
            for i in range(0, n):
                self.rois.append(ROI(sources == i, image=self.image,
                                    name=f"ROI_{i}", affine=self.image.affine))
            self.loaded = True

        elif not skrt.core.is_list(sources):
            sources = [sources]

        # Expand any directories
        sources_expanded = []
        for source in sources:
            if isinstance(source, str) and os.path.isdir(source):
                sources_expanded.extend(
                    [os.path.join(source, file) for file in os.listdir(source)]
                )
            elif not self.loaded:
                sources_expanded.append(source)

        for source in sources_expanded:

            if isinstance(source, ROI):
                self.rois.append(source)
                continue

            if isinstance(source, str):
                if os.path.basename(source).startswith(".") or source.endswith(".txt"):
                    continue
                if os.path.isdir(source):
                    continue

            # Attempt to load from dicom
            rois = []
            if isinstance(source, str):
                rois = load_rois_dicom(source)
            if len(rois):
                for roi in rois.values():
                    self.rois.append(
                        ROI(
                            roi["contours"],
                            name=roi["name"],
                            color=roi["color"],
                            image=self.image,
                        )
                    )

            # Load from ROI mask
            else:
                try:
                    self.rois.append(ROI(source, image=self.image))
                except RuntimeError:
                    continue

        self.rename_rois()
        self.filter_rois()
        for roi in self.rois:
            roi.structure_set = self

        self.loaded = True

    def reset(self):
        """Reload structure set from original source(s)."""

        self.rois = []
        self.loaded = False
        self.load(force=True)

    def set_image(self, image):
        """Set image for self and all ROIs."""

        if image and not isinstance(image, skrt.image.Image):
            image = skrt.image.Image(image)

        self.image = image
        for s in self.rois:
            s.image = image

    def rename_rois(
        self, names=None, first_match_only=True, keep_renamed_only=False
    ):
        """Rename ROIs if a naming dictionary is given. If
        <first_match_only> is True, only the first ROI matching the
        possible matches will be renamed."""

        if names is None:
            names = self.names
        if not names:
            return

        # Loop through each new name
        already_renamed = []
        for name, matches in names.items():

            if not skrt.core.is_list(matches):
                matches = [matches]

            # Loop through all possible original names
            name_matched = False
            for m in matches:

                # Loop through ROIs and see if there's a match
                for i, s in enumerate(self.rois):

                    # Don't rename an ROI more than once
                    if i in already_renamed:
                        continue

                    if fnmatch.fnmatch(s.name.lower(), m.lower()):
                        s.name = name
                        name_matched = True
                        already_renamed.append(i)
                        if first_match_only:
                            break

                # If first_match_only, don't rename more than one ROI
                # with this new name
                if name_matched and first_match_only:
                    break

        # Keep only the renamed ROIs if requested
        if keep_renamed_only:
            renamed_rois = [self.rois[i] for i in already_renamed]
            self.rois = renamed_rois

    def filter_rois(self, to_keep=None, to_remove=None):
        """Keep only the ROIs in the to_keep list and remove any in the
        to_remove list."""

        if to_keep is None:
            to_keep = self.to_keep
        elif not skrt.core.is_list(to_keep):
            to_keep = [to_keep]
        if to_remove is None:
            to_remove = self.to_remove
        elif not skrt.core.is_list(to_remove):
            to_remove = [to_remove]

        if to_keep is not None:
            keep = []
            for s in self.rois:
                if any([fnmatch.fnmatch(s.name.lower(), k.lower()) for k in to_keep]):
                    keep.append(s)
            self.rois = keep

        if to_remove is not None:
            keep = []
            for s in self.rois:
                if not any(
                    [fnmatch.fnmatch(s.name.lower(), r.lower()) for r in to_remove]
                ):
                    keep.append(s)
            self.rois = keep

    def add_rois(self, sources):
        """Add additional ROIs from source(s)."""

        if not skrt.core.is_list(sources):
            sources = [sources]
        self.sources.extend(sources)
        self.load(sources)

    def add_roi(self, source, **kwargs):
        """Add a single ROI with  optional kwargs."""

        self.sources.append(source)
        if isinstance(source, ROI):
            roi = source
        else:
            roi = ROI(source, **kwargs)
        roi.structure_set = self
        self.rois.append(roi)

    def filter(
        self,
        names=None,
        name=None,
        to_keep=None,
        to_remove=None,
        keep_renamed_only=False,
    ):
        """Create a copy of this structure set with ROIs optionally
        renamed or filtered. Returns a new StructureSet object."""

        if not hasattr(self, "n_copies"):
            self.n_copies = 1
        else:
            self.n_copies += 1
        if name is None:
            name = f"{self.name} (copy {self.n_copies})"

        ss = StructureSet(
            self.sources,
            name=name,
            image=self.image,
            load=False,
            names=names,
            to_keep=to_keep,
            to_remove=to_remove,
        )
        if self.loaded:
            ss.rois = self.rois
            ss.loaded = True
            ss.rename_rois(names, keep_renamed_only=keep_renamed_only)
            ss.filter_rois(to_keep, to_remove)

        return ss

    def get_rois(self, names=None):
        """Get list of ROI objects If <names> is given, only the ROIs with
        those names will be returned."""

        self.load()
        if names is None:
            return self.rois

        rois = []
        for name in names:
            roi = self.get_roi(name)
            if roi is not None:
                rois.append(roi)
        return rois

    def get_rois_wildcard(self, wildcard):
        """Return list of ROIs matching a wildcard expression."""

        rois = []
        for roi in self.get_rois():
            if fnmatch.fnmatch(roi.name, wildcard):
                rois.append(roi)
        return rois

    def get_roi_names(self, original=False):
        """
        Get list of names of ROIs in this structure set. If <original> is True,
        get the original names of the ROIs.
        """

        if not original:
            return [s.name for s in self.get_rois()]
        else:
            return [s.original_name for s in self.get_rois()]

    def get_roi_dict(self):
        """Get dict of ROI names and objects."""

        return {s.name: s for s in self.get_rois()}

    def get_roi(self, name):
        """Get an ROI with a specific name."""

        rois = self.get_roi_dict()
        if name not in rois:
            print(f"ROI {name} not found!")
            return
        return rois[name]

    def print_rois(self):

        self.load()
        print("\n".join(self.get_roi_names()))

    def __repr__(self):

        self.load()
        out_str = "StructureSet\n{"
        out_str += "\n  name : " + str(self.name)
        out_str += "\n  ROIs :\n    "
        out_str += "\n    ".join(self.get_roi_names())
        out_str += "\n}"
        return out_str

    def get_geometry(self, **kwargs):
        """Get pandas DataFrame of geometric properties for all ROIs."""

        return pd.concat([s.get_geometry(**kwargs) for s in self.get_rois()])

    def get_comparison(self, other=None, method=None, **kwargs):
        """Get pandas DataFrame of comparison metrics vs a single ROI or
        another StructureSet."""

        dfs = []
        if isinstance(other, ROI):
            dfs = [s.get_comparison(other, **kwargs) for s in self.get_rois()]

        elif isinstance(other, StructureSet) or other is None:
            pairs = self.get_comparison_pairs(other, method)
            dfs = []
            for roi1, roi2 in pairs:
                dfs.append(roi1.get_comparison(roi2, **kwargs))

        else:
            raise TypeError("<other> must be ROI or StructureSet!")

        return pd.concat(dfs)

    def get_comparison_pairs(self, other=None, method=None):
        """Get list of ROIs to compare with one another."""

        if other is None:
            other = self
            if method is None:
                method = "diff"
        elif method is None:
            method = "auto"

        # Check for name matches
        matches = []
        if method in ["auto", "named"]:
            matches = [
                s for s in self.get_roi_names() if s in other.get_roi_names()
            ]
            if len(matches) or method == "named":
                return [
                    (self.get_roi(name), other.get_roi(name)) for name in matches
                ]

        # Otherwise, pair each ROI with every other
        pairs = []
        for roi1 in self.get_rois():
            for roi2 in other.get_rois():
                pairs.append((roi1, roi2))

        # Remove matching names if needed
        if method == "diff":
            pairs = [p for p in pairs if p[0].name != p[1].name]

        return pairs

    def plot_comparisons(
        self, other=None, method=None, outdir=None, legend=True, **kwargs
    ):
        """Plot comparison pairs."""

        if outdir and not os.path.exists(outdir):
            os.makedirs(outdir)

        for roi1, roi2 in self.get_comparison_pairs(other, method):

            outname = None
            if outdir:
                comp_name = roi1.get_comparison_name(roi2, True)
                outname = os.path.join(outdir, f"{comp_name}.png")

            names = None
            if roi1.name == roi2.name:
                names = [self.name, other.name]

            roi1.plot_comparison(
                roi2, legend=legend, save_as=outname, names=names, **kwargs
            )

    def plot_surface_distances(
        self, other, outdir=None, signed=False, method="auto", **kwargs
    ):
        """Plot surface distances for all ROI pairs."""

        if not os.path.exists(outdir):
            os.makedirs(outdir)

        for roi1, roi2 in self.get_comparison_pairs(other, method):
            comp_name = roi1.get_comparison_name(roi2, True)
            if outdir:
                outname = os.path.join(outdir, f"{comp_name}.png")
            else:
                outname = None
            roi1.plot_surface_distances(roi2, signed=signed, save_as=outname, **kwargs)

    def write(self, outname=None, outdir=".", ext=None, overwrite=False, **kwargs):
        """Write to a dicom StructureSet file or directory of nifti files."""

        if ext is not None and not ext.startswith("."):
            ext = f".{ext}"

        # Check whether to write to dicom file
        if isinstance(outname, str) and outname.endswith(".dcm"):
            ext = ".dcm"
            outname = os.path.join(outdir, outname)

        if ext == ".dcm":
            if outname is None:
                outname = f"{outdir}/{self.name}.dcm"
            print("Warning: dicom writing not yet available!")
            return

        # Otherwise, write to individual ROI files
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        elif overwrite:
            shutil.rmtree(outdir)
            os.mkdir(outdir)
        for s in self.get_rois():
            s.write(outdir=outdir, ext=ext, **kwargs)

    def get_staple(self, **kwargs):
        """Apply STAPLE to all ROIs in this structure set and return
        STAPLE contour as an ROI."""

        # Get staple mask
        import SimpleITK as sitk
        rois = []
        for s in self.rois:
            s.create_mask()
            rois.append(sitk.GetImageFromArray(s.sdata.astype(int)))
        probs = sitk.GetArrayFromImage(sitk.STAPLE(rois, 1))
        mask = probs > 0.95

        # Create staple ROI
        staple = ROI(
            mask, 
            name="staple", 
            image=self.image,
            affine=self.rois[0].saffine,
            **kwargs
        )

        # Return staple ROI
        return staple


class StructureSetIterator:

    def __init__(self, structure_set):
        self.idx = -1
        self.structure_set = structure_set

    def __next__(self):
        self.idx += 1
        if self.idx < len(self.structure_set.get_rois()):
            return self.structure_set.get_rois()[self.idx]
        raise StopIteration


def load_rois_dicom(path, names=None):
    """Load ROI(s) from a dicom structure set file. <name> can be a single
    name or list of names of ROIs to load."""

    # Load dicom object
    try:
        ds = pydicom.read_file(path, force=True)
    except pydicom.errors.InvalidDicomError:
        return []
    if not hasattr(ds, "SOPClassUID"):
        return []
    if not (ds.SOPClassUID == "1.2.840.10008.5.1.4.1.1.481.3"):
        print(f"Warning: {path} is not a DICOM structure set file!")
        return []

    # Get ROI names
    seq = get_dicom_sequence(ds, "StructureSetROI")
    rois = {}
    for roi in seq:
        rois[int(roi.ROINumber)] = {"name": roi.ROIName}

    # Find ROIs matching requested names
    names_to_load = None
    if isinstance(names, str):
        names_to_load = [names]
    elif skrt.core.is_list(names):
        names_to_load = names
    if names_to_load:
        rois = {
            i: s
            for i, s in rois.items()
            if any(
                [fnmatch.fnmatch(s["name"].lower(), n.lower()) for n in names_to_load]
            )
        }
        if not len(rois):
            print(f"Warning: no ROIs found matching name(s): {names}")
            return

    # Get ROI details
    roi_seq = get_dicom_sequence(ds, "ROIContour")
    for roi in roi_seq:

        number = roi.ReferencedROINumber
        if number not in rois:
            continue
        data = {"contours": {}}

        # Get ROI colour
        if "ROIDisplayColor" in roi:
            data["color"] = [int(c) / 255 for c in list(roi.ROIDisplayColor)]
        else:
            data["color"] = None

        # Get contours
        contour_seq = get_dicom_sequence(roi, "Contour")
        if contour_seq:
            for c in contour_seq:
                plane_data = [
                    [float(p) for p in c.ContourData[i * 3 : i * 3 + 3]]
                    for i in range(c.NumberOfContourPoints)
                ]
                z = float(c.ContourData[2])
                if z not in data["contours"]:
                    data["contours"][z] = []
                data["contours"][z].append(np.array(plane_data))

        rois[number].update(data)

    return rois


def get_dicom_sequence(ds=None, basename=""):

    sequence = []
    for suffix in ["Sequence", "s"]:
        attribute = f"{basename}{suffix}"
        if hasattr(ds, attribute):
            sequence = getattr(ds, attribute)
            break
    return sequence


def write_structure_set_dicom(
    outname, 
    rois, 
    image=None, 
    affine=None, 
    shape=None,
    orientation=None, 
    header_source=None, 
    patient_id=None,
    modality=None, 
    root_uid=None
):

    # Check we have the relevant info
    if not image and (not affine or not shape):
        raise RuntimeError("Must provide either an image or an affine matrix "
                           "and shape!")

    # Try getting dicom dataset from image
    ds = None
    if image:
        if hasattr(image, "dicom_dataset"):
            ds = image.dicom_dataset
        else:
            ds = skrt.image.create_dicom()
            ds.set_geometry(
                image.get_affine(), image.get_data().shape,
                image.get_orientation_vector(image.get_affine, "dicom")
            )

    # Otherwise, create fresh dicom dataset
    else:
        ds = skrt.image.create_dicom(patient_id, modality, root_uid)
        ds.set_geometry(affine, shape, orientation)

    # Adjust dataset to be for StructureSet instead of image


def dicom_dataset_to_structure_set(ds):
    '''Convert an existing image dicom dataset to a StructureSet dataset.'''

    # Adjust class UIDs
    ds.file_meta.ImplementationClassUID = "9.9.9.100.0.0.1.0.9.6.0.0.1"
    ds.file_meta.MediaStorageSOPClassUID = "1.2.840.10008.5.1.4.1.1.481.3"

    # Assign empty sequences
    ds.ReferencedFrameofReferenceSequence = Sequence()
    ds.StructureSetROISequence = Sequence()
    ds.RTROIObservationsSequence = Sequence()
    ds.ROIContourSequence = Sequence()

    # Assign structure set properties
    ds.StructureSetLabel = ""
    ds.StructureSetDate = ds.InstanceCreationDate
    ds.StructureSetTime = ds.InstanceCreationTime

    # Assign frame of reference
