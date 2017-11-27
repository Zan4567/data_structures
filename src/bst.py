'''Binary search tree implementation.'''
from collections import Iterable


class BSTNode(object):
    '''Node of the binary search tree.'''
    def __init__(self, val):
        '''.'''
        self.value = val
        self.left = None
        self.right = None


class BinarySearchTree(object):
    '''Binary search Tree.'''
    def __init__(self, start_data=None):
        '''Constructor. Initialize by passing an iterable to start_data'''
        self.root = None
        self._size = 0
        if isinstance(start_data, Iterable):
            for value in start_data:
                self.insert(value)

    def insert(self, val):
        '''Insert a value into the tree.'''
        if self.root is None:
            self.root = BSTNode(val)
            self._size = 1
            return
        parent = self._get_nearest_node(val)
        if parent.value == val:
            return
        if val < parent.value:
            parent.left = BSTNode(val)
            self._size += 1
        if val > parent.value:
            parent.right = BSTNode(val)
            self._size += 1

    def _get_nearest_node(self, val):
        '''helper function. Guarentees that the returned node is either the
        same as the given value, or the appropriate parent for it.'''
        node = self.root
        if node is None:
            return None
        while node.value != val:
            if val < node.value and node.left is not None:
                node = node.left
            elif val > node.value and node.right is not None:
                node = node.right
            else:
                return node
        return node

    def search(self, val):
        '''Return a node with the specified value. Returns None if not found'''
        node = self._get_nearest_node(val)
        if node and node.value == val:
            return node
        return None

    def size(self):
        '''Get the size of the tree.'''
        return self._size

    def __len__(self):
        '''Used by the len() function.'''
        return self._size

    def depth(self):
        '''Gets the depth of the tree.'''
        return self._get_depth(self.root)

    def _get_depth(self, node):
        '''Recursively finds the depth of the tree.'''
        if node is None:
            return -1
        left = self._get_depth(node.left)
        right = self._get_depth(node.right)
        if left > right:
            return left + 1
        else:
            return right + 1

    def contains(self, val):
        '''Returns if the specified value is in the tree.'''
        if self.search(val):
            return True
        return False

    def balance(self):
        '''Returns the balance of the tree: depth of the right branch minus
        the depth of the left branch'''
        if self.root:
            return (self._get_depth(self.root.right) -
                    self._get_depth(self.root.left))
        return 0

if __name__ == '__main__':
    import timeit
    balanced = BinarySearchTree(
        [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9,
         11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])
    unbalanced = BinarySearchTree([i for i in range(1, 32)])

    balanced_time = min(timeit.repeat(
        stmt="balanced.search(31)",
        setup="from bst import BinarySearchTree; balanced = BinarySearchTree( \
        [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7,\
        9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])"))
    unbalanced_time = min(timeit.repeat(
        stmt="unbalanced.search(31)",
        setup="from bst import BinarySearchTree;\
        unbalanced = BinarySearchTree([i for i in range(1, 32)])"))

    print('Time to search a balanced tree: ' + str(balanced_time))
    print('Time to search an unbalanced tree: ' + str(unbalanced_time))
