'''.'''


class Linked_List(object):
    '''.'''

    def __init__(self, itr=()):
        self.head = None
        self._size = 0
        if isinstance(itr, (str, tuple, list)):
            for item in itr:
                self.push(item)

    def push(self, val):
        '''.'''
        new_head = Node(val)
        new_head.next_node = self.head
        self.head = new_head
        self._size += 1

    def pop(self):
        '''.'''
        pop_node = self.head
        if pop_node is None:
            raise IndexError('No nodes in list')
        self.head = pop_node.next_node
        pop_node.next_node = None
        self._size -= 1
        return pop_node.value

    def size(self):
        '''.'''
        return self._size

    def size2(self):  # pragma no cover
        '''.'''
        count = 0
        count_node = self.head
        while(count_node):
            count += 1
            count_node = count_node.next_node
        return count

    def __len__(self):
        '''.'''
        return self.size()

    def search(self, val):
        '''.'''
        search_node = self.head
        while(search_node):
            if search_node.value == val:
                return search_node
            search_node = search_node.next_node
        return None

    def remove(self, node):
        '''.'''
        search_node = self.head
        while(search_node):
            if search_node.next_node == node:
                search_node.next_node = node.next_node
                node.next_node = None
                self._size -= 1
                return
            search_node = search_node.next_node

    def display(self):
        '''.'''
        string_list = '('
        current_node = self.head
        while current_node:
            string_list = string_list + current_node.value
            if current_node.next_node:
                string_list = string_list + ', '
            current_node = current_node.next_node

        string_list = string_list + ')'
        return string_list


class Node(object):
    '''.'''
    def __init__(self, val=None):
        self.next_node = None
        self.value = val
