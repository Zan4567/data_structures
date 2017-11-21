'''.'''


class BSTNode(object):
    '''.'''
    def __init__(self, val):
        '''.'''
        self.value = val
        self.left = None
        self.right = None


class BinarySearchTree(object):
    '''.'''
    def __init__(self, start_data=None):
        '''.'''
        self.root = None
        self._size = 0

    def insert(self, val):
        '''.'''
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
        '''.'''
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
        '''.'''
        node = self._get_nearest_node(val)
        if node.value == val:
            return node
        return None

    def size(self):
        '''.'''
        return self._size

    def __len__(self):
        '''.'''
        return self._size

    def depth(self):
        '''.'''
        return self._get_depth(self.root)

    def _get_depth(self, node):
        '''.'''
        if node is None:
            return -1
        left = self._get_depth(node.left)
        right = self._get_depth(node.right)
        if left > right:
            return left + 1
        else:
            return right + 1

    def contains(self, val):
        '''.'''
        if self.search(val):
            return True
        return False

    def balance(self):
        '''.'''
        if root:
            return self._get_depth(root.right) - self._get_depth(root.left)
        return 0
