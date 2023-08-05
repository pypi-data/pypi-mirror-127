"""Core data classes and functions."""

import copy
import functools
import numpy as np
import os
import time
from logging import getLogger, Formatter, StreamHandler
from typing import Any, List, Optional, Tuple


class Defaults:
    """
    Singleton class for storing default values of parameters
    that may be used in object initialisation.

    Implementation of the singleton design pattern is based on:
    https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    """

    # Define the single instance as a class attribute
    instance = None

    # Create single instance in inner class
    class __Defaults:

        def __init__(self, opts: Optional[dict] = None):
            """Define instance attributes based on opts dictionary."""

            if opts:
                for key, value in opts.items():
                    setattr(self, key, value)

        def __repr__(self):
            """Print instance attributes."""

            out = []
            for key, value in sorted(self.__dict__.items()):
                out_list.append(f"{key}: {value}")
            return "\n".join(out)

    def __init__(self, opts: Optional[dict] = None, reset: bool = False):
        """
        Constructor of Defaults singleton class.

        Parameters
        ----------
        opts: dict, default={}
            Dictionary of attribute-value pairs.

        reset: bool, default=False
            If True, delete all pre-existing instance attributes before
            adding attributes and values from opts dictionary.
            If False, don't delete pre-existing instance attributes,
            but add to them, or modify values, from opts dictionary.
        """

        if not Defaults.instance:
            Defaults.instance = Defaults.__Defaults(opts)
        else:
            if reset:
                Defaults.instance.__dict__ = {}
            if opts:
                for key, value in opts.items():
                    setattr(Defaults.instance, key, value)

    def __getattr__(self, name: str):
        """Get instance attributes."""

        return getattr(self.instance, name)

    def __setattr__(self, name: str, value: Any):
        """Set instance attributes."""

        return setattr(self.instance, name, value)

    def __repr__(self):
        """Print instance attributes."""

        return self.instance.__repr__()


# Initialise default parameter values:
Defaults()

# Depth to which recursion is performed when printing instances
# of classes that inherit from the Data class.
Defaults({"print_depth": 0})

# Severity level for event logging.
# Defined values are: 'NOTSET' (0), 'DEBUG' (10), 'INFO' (20),
# 'WARNING' (30), 'ERROR' (40), 'CRITICAL' (50)
Defaults({"log_level": "WARNING"})


class Data:
    """
    Base class for objects serving as data containers.
    An object has user-defined data attributes, which may include
    other Data objects and lists of Data objects.

    The class provides for printing attribute values recursively, to
    a chosen depth, and for obtaining nested dictionaries of
    attributes and values.
    """

    def __init__(self, opts: Optional[dict] = None, **kwargs):
        """
        Constructor of Data class, allowing initialisation of an
        arbitrary set of attributes.

        Parameters
        ----------
        opts: dict, default={}
            Dictionary to be used in setting instance attributes
            (dictionary keys) and their initial values.

        **kwargs
            Keyword-value pairs to be used in setting instance attributes
            and their initial values.
        """

        if opts:
            for key, value in opts.items():
                setattr(self, key, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self, depth: Optional[int] = None) -> str:
        """
        Create string recursively listing attributes and values.

        Parameters
        ----------

        depth: integer/None, default=None
            Depth to which recursion is performed.
            If the value is None, depth is set to the value
            of the object's print_depth property, if defined,
            or otherwise to the value of Defaults().print_depth.
        """

        if depth is None:
            depth = self.get_print_depth()

        out = [f"\n{self.__class__.__name__}", "{"]

        # Loop over attributes, with different treatment
        # depending on whether attribute value is a list.
        # Where an attribute value of list item is
        # an instance of Data or a subclass
        # it's string representation is obtained by calling
        # the instance's __repr__() method with depth decreased
        # by 1, or (depth less than 1) is the class representation.
        for key in sorted(self.__dict__):

            # Ignore private attributes 
            if key.startswith("_"):
                continue

            item = self.__dict__[key]

            # Handle printing of numpy arrays
            if isinstance(item, np.ndarray):
                value_string = f"{item.shape} array"

            # Handle printing of lists
            elif isinstance(item, list):
                items = item
                n = len(items)
                if n:
                    if depth > 0:
                        value_string = "["
                        for i, item in enumerate(items):
                            try:
                                item_string = item.__repr__(depth=(depth - 1))
                            except TypeError:
                                item_string = item.__repr__()
                            comma = "," if (i + 1 < n) else ""
                            value_string = f"{value_string} {item_string}{comma}"
                        value_string = f"{value_string}]"
                    else:
                        value_string = f"[{n} * {item[0].__class__}]"
                else:
                    value_string = "[]"

            # Handle printing of dicts
            elif isinstance(item, dict):
                items = item
                n = len(items)
                if n:
                    if depth > 0:
                        value_string = "{"
                        for i, (key, value) in enumerate(items.items()):
                            item_string = "{key}: "
                            try:
                                item_string += item.__repr__(depth=(depth - 1))
                            except TypeError:
                                item_string += item.__repr__()
                            comma = "," if (i + 1 < n) else ""
                            value_string = f"{value_string} {item_string}{comma}"
                        value_string = f"{{{value_string}}}"
                    else:
                        value_string = f"{{{n} * keys of type {list(item.keys())[0].__class__}}}"
                else:
                    value_string = "{}"

            # Handle printing of nested Data objects
            else:
                if issubclass(item.__class__, Data):
                    if depth > 0:
                        value_string = item.__repr__(depth=(depth - 1))
                    else:
                        value_string = f"{item.__class__}"
                else:
                    value_string = item.__repr__()
            out.append(f"  {key}: {value_string} ")

        out.append("}")
        return "\n".join(out)

    def clone(self):
        """
        Return a clone of the Data object containing copies of any 
        lists, dicts, or arrays owned by the object.
        """

        clone = copy.copy(self)
        self.clone_attrs(clone)
        return clone

    def clone_attrs(self, obj):
        """
        Apply class attributes from self to a new object, making copies 
        of any lists, dicts, or numpy arrays.
        """

        for attr in dir(self):

            # Don't copy private variables
            if attr.startswith("__"):
                continue

            # Don't copy methods
            if callable(getattr(self, attr)):
                continue
            
            # Make new copy of lists/dicts/arrays
            if type(getattr(self, attr)) in [list, dict, np.ndarray]:
                setattr(obj, attr, copy.copy(getattr(self, attr)))

            # Otherwise, copy reference to attribute
            else:
                setattr(obj, attr, getattr(self, attr))

    def get_dict(self) -> dict:
        """
        Return a nested dictionary of object attributes (dictionary keys)
        and their values.
        """

        objects = {}
        for key in self.__dict__:
            try:
                objects[key] = self.__dict__[key].get_dict()
            except AttributeError:
                objects[key] = self.__dict__[key]

        return objects

    def get_print_depth(self) -> int:
        """
        Retrieve the value of the object's print depth,
        setting an initial value if not previously defined.
        """

        if not hasattr(self, "print_depth"):
            self.set_print_depth()
        return self.print_depth

    def print(self, depth: Optional[int] = None):
        """
        Convenience method for recursively printing
        object attributes and values, with recursion
        to a specified depth.

        Parameters
        ----------

        depth: integer/None, default=None
            Depth to which recursion is performed.
            If the value is None, depth is set in the
            __repr__() method.
        """

        print(self.__repr__(depth))

    def set_print_depth(self, depth: Optional[int] = None):
        """
        Set the object's print depth.

        Parameters
        ----------

        depth: integer/None, default=None
            Depth to which recursion is performed.
            If the value is None, the object's print depth is
            set to the value of Defaults().print_depth.
        """

        if depth is None:
            depth = Defaults().print_depth
        self.print_depth = depth


class PathData(Data):
    """Data with an associated path or directory; has the ability to
    extract a list of dated objects from within this directory."""

    def __init__(self, path=""):
        self.path = fullpath(path)
        self.subdir = ""

    def get_dated_objects(self, 
                          dtype: type, 
                          subdir: str = "", 
                          **kwargs) -> List[Any]:
        """Create list of objects of a given type, <dtype>, inside own
        directory, or inside own directory + <subdir> if given."""

        # Create object for each file in the subdir
        objs = []
        path = os.path.join(self.path, subdir)
        if os.path.isdir(path):
            for filename in os.listdir(path):
                if is_timestamp(filename):
                    filepath = os.path.join(path, filename)
                    try:
                        objs.append(dtype(path=filepath, **kwargs))
                    except RuntimeError:
                        pass

        # Sort and assign subdir to the created objects
        objs.sort()
        if subdir:
            for obj in objs:
                obj.subdir = subdir

        return objs


@functools.total_ordering
class Dated(PathData):
    """PathData with an associated date and time, which can be used for
    sorting multiple Dateds."""

    def __init__(self, path: str = "", auto_timestamp=False):
        """
        Initialise dated object from a path and assign its timestamp. If 
        no valid timestamp is found within the path string, it will be set 
        automatically from the current date and time if auto_timestamp is True.
        """

        PathData.__init__(self, path)

        # Assign date and time
        timestamp = os.path.basename(self.path)
        self.date, self.time = get_time_and_date(timestamp)
        if (self.date is None) and (self.time is None):
            timestamp = os.path.basename(os.path.dirname(self.path))
            self.date, self.time = get_time_and_date(timestamp)
        if (self.date is None) and (self.time is None):
            timestamp = os.path.basename(self.path)
            try:
                self.date, self.time = timestamp.split("_")
            except ValueError:
                self.date, self.time = (None, None)

        # Set date and time from current time
        if not self.date and auto_timestamp:
            self.date = time.strftime("%Y%m%d")
            self.time = time.strftime("%H%M%S")

        # Make full timestamp string
        self.timestamp = f"{self.date}_{self.time}"

    def in_date_interval(self, 
                         min_date: Optional[str] = None, 
                         max_date: Optional[str] = None) -> bool:
        """Check whether own date falls within an interval."""

        if min_date:
            if self.date < min_date:
                return False
        if max_date:
            if self.date > max_date:
                return False
        return True

    def __eq__(self, other):
        return self.date == other.date and self.time == other.time

    def __ne__(self, other):
        return self.date == other.date or self.time == other.time

    def __lt__(self, other):
        if self.date == other.date:
            return self.time < other.time
        return self.date < other.date

    def __gt__(self, other):
        if self.date == other.date:
            return self.time > other.time
        return self.date > other.date

    def __le__(self, other):
        if self.date == other.date:
            return self.time < other.time
        return self.date < other.date


class MachineData(Dated):
    """Dated object with an associated machine name."""

    def __init__(self, path: str = ""):
        Dated.__init__(self, path)
        self.machine = os.path.basename(os.path.dirname(path))


class Archive(Dated):
    """Dated object associated with multiple files."""

    def __init__(self, path: str = "", allow_dirs: bool = False):

        Dated.__init__(self, path)

        # Find names of files within the directory
        self.files = []
        try:
            filenames = os.listdir(self.path)
        except OSError:
            filenames = []

        for filename in filenames:

            # Disregard hidden files
            if not filename.startswith("."):
                filepath = os.path.join(self.path, filename)

                # Disregard directories unless allow_dirs is True
                if not os.path.isdir(filepath) or allow_dirs:
                    self.files.append(File(path=filepath))

        self.files.sort()


class File(Dated):
    """File with an associated date. Files can be sorted based on their
    filenames."""

    def __init__(self, path: str = ""):
        Dated.__init__(self, path)

    def __eq__(self, other):
        return self.path == other.path

    def __ne__(self, other):
        return self.path != other.path

    def __lt__(self, other):

        self_name = os.path.splitext(os.path.basename(self.path))[0]
        other_name = os.path.splitext(os.path.basename(other.path))[0]
        try:
            result = eval(self_name) < eval(other_name)
        except (NameError, SyntaxError):
            result = self.path < other.path
        return result

    def __gt__(self, other):

        self_name = os.path.splitext(os.path.basename(self.path))[0]
        other_name = os.path.splitext(os.path.basename(other.path))[0]
        try:
            result = eval(self_name) > eval(other_name)
        except (NameError, SyntaxError):
            result = self.path > other.path
        return result


def alphanumeric(in_str: str = "") -> List[str]:
    """Function that can be passed as value for list sort() method
    to have alphanumeric (natural) sorting"""

    import re

    elements = []
    for substr in re.split("(-*[0-9]+)", in_str):
        try:
            element = int(substr)
        except BaseException:
            element = substr
        elements.append(element)
    return elements


def fullpath(path: str = "") -> str:
    """Evaluate full path, expanding '~', environment variables, and
    symbolic links."""

    expanded = ""
    if path:
        tmp = os.path.expandvars(path.strip())
        tmp = os.path.abspath(os.path.expanduser(tmp))
        expanded = os.path.realpath(tmp)
    return expanded

def get_logger(name="", log_level=None):
    """
    Retrieve named event logger.

    Parameters
    ----------
    name: string, default=""
        Name of logger (see documentation of logging module)
    log_level: string/integer/None, default=None
        Severity level for event logging.  If the value is None,
        log_level is set to the value of Defaults().log_level.
    """
    formatter = Formatter("%(name)s - %(levelname)s - %(message)s")
    handler = StreamHandler()
    handler.setFormatter(formatter)
    logger = getLogger(name)
    if not logger.handlers:
        logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger

def get_time_and_date(timestamp: str = "") -> Tuple[str, str]:
    """Extract time and date separately from timestamp."""

    time_date = (None, None)
    if is_timestamp(timestamp):
        items = os.path.splitext(timestamp)[0].split("_")
        items = [item.strip() for item in items]
        if items[0].isalpha():
            time_date = tuple(items[1:3])
        else:
            time_date = tuple(items[0:2])
    else:
        i1 = timestamp.find("_")
        i2 = timestamp.rfind(".")
        if (-1 != i1) and (-1 != i2):
            bitstamp = timestamp[i1 + 1: i2]
            if is_timestamp(bitstamp):
                time_date = tuple(bitstamp.split("_"))

    return time_date


def is_timestamp(string: str = "") -> bool:
    """Check whether a string is a valid timestamp."""

    valid = True
    items = os.path.splitext(string)[0].split("_")
    items = [item.strip() for item in items]
    if len(items) > 2:
        if items[0].isalpha() and items[1].isdigit() and items[2].isdigit():
            items = items[1:3]
        elif items[0].isdigit() and items[1].isdigit():
            items = items[:2]
        elif items[0].isdigit() and items[1].isdigit():
            items = items[:2]
    if len(items) != 2:
        valid = False
    else:
        for item in items:
            if not item.isdigit():
                valid = False
                break
    return valid


def is_list(var: Any) -> bool:
    """Check whether a variable is a list, tuple, or array."""

    is_a_list = False
    for t in [list, tuple, np.ndarray]:
        if isinstance(var, t):
            is_a_list = True
    return is_a_list


def to_three(val: Any) -> Optional[List]:
    """Ensure that a value is a list of three items."""

    if val is None:
        return None
    if is_list(val):
        if not len(val) == 3:
            print(f"Warning: {val} should be a list containing 3 items!")
        return list(val)
    elif not is_list(val):
        return [val, val, val]


def generate_timestamp() -> str:
    '''Make timestamp from the current time.'''

    return time.strftime('%Y%m%d_%H%M%S')
