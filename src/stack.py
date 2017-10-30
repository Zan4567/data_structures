"""A stack with push and pop methods"""

from linked_list import Linked_List


class Stack(object):
    """A Stack - first in last out"""
    def __init__(self):
        """The stack is composed of the Linked_List."""
        self.stack = Linked_List()
