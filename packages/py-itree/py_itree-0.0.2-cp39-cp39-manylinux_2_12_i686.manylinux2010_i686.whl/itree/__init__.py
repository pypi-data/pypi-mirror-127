from .version import __version__

try:
    from . import _itree
except ImportError:
    import _itree

import time
from subprocess import check_call
from tempfile import NamedTemporaryFile
import random

class Node(_itree.Node):
    """Tree Node

    Node is a nary interval tree node with the following member variables:

    .. highlight:: python
    .. code-block:: python

        nid - node id, unique in a tree
        name - node name
        start - start value
        end - end value
        extra - a dictionary of extra information
        nodes - children of the current node

    When value is time itself, the start and end are timestamps. When value is not time, for instance network traffic, the time stamp can be stored in the extra dictionary.
    """

def _consolidate(node: Node):
    if isinstance(node, Node):
        return _itree.consolidate(node)
    return None

class Tree(_itree.Tree):
    """An interval tree"""

    def __init__(self, tid=None, extra={}, monotonic=True, capacity=1024, zsn_threshold=1e-7):
        """Constructor of Tree

        Args:
            tid (str, optional): a unique id of the tree. Defaults to None.
            extra (dict, optional): extra information of the tree. Defaults to {}.
        """
        if tid is None:
            tid = "{:08x}".format(random.getrandbits(32))

        super().__init__(tid=tid, extra=extra, monotonic=monotonic, capacity=capacity, zsn_threshold=zsn_threshold)

    def start(self, a, b, extra={}):
        """discover a node with name `a` and value `b`, and extra"""
        self.discover(a, b, extra)

    def end(self, a, b, extra={}):
        """finish a node with name `a` and value `b`, and extra"""
        self.finish(a, b, extra)

    def consolidate(self):
        """consolidate virtual nodes if any"""
        if len(self.stk) > 1:
            return
        self.root = _consolidate(self.root)

    def to_img(sf, filename=None, format="png", node_shape="record"):
        """Render tree to an image with `dot`"""
        try:
            if not filename:
                filename = f"/tmp/{time.time()}.{format}"
            s = sf.to_dot_string(node_shape)
            with NamedTemporaryFile("wb", delete=True) as dotfile:
                dotfilename = dotfile.name
                dotfile.write(s.encode("utf-8"))
                dotfile.flush()
                cmd = ["dot", dotfilename, "-T", format, "-o", filename]
                check_call(cmd)
        except FileNotFoundError as e:
            print("dot is missing! please install graphviz.")
            return None
        return filename


# ForestStats is a collection of trees
ForestStats=_itree.ForestStats

nemo_transform = _itree.nemo_transform
uuid = _itree.uuid
mod = _itree.mod

exe = _itree._exe
time_s = _itree.time_s
time_ms = _itree.time_ms
time_us = _itree.time_us
is_virtual_node = _itree.is_virtual_node
