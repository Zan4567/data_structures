'''.'''

class Linked_List(object):
    '''.'''

    def __init__(self, itr = ()):
        self.head = None
        self._size = 0
        if isinstance(itr, (str, tuple, list))
            for item in itr:
                push(item)
                
    def push(val):
        '''.'''
        new_head = Node(val)
        new_head.next_node = self.head
        self.head = new_head
        self._size += 1

    def pop():
        '''.'''
        pop_node = self.head
        if pop_node is None: raise IndexError('No nodes in list')
        self.head = pop_node.next_node
        pop_node.next_node = None
        self._size -= 1
        return pop_node.value

    def size():
        '''.'''
        return _size

    def size2():
        '''.'''
        count = 0
        count_node = self.head
        while(count_node):
            count += 1
            count_node = count_node.next_node
        return count

    def __len__():
        '''.'''
        return size()

    def search(val):
        '''.'''
        search_node = self.head
        while(search_node):
            if search_node.value == val: return search_node
            search_node = search_node.next_node
        return None

    def remove(node):
        '''.'''
        search_node = self.head
        while(search_node):
            if search_node.next_node == node:
                search_node.next_node = node.next_node
                node.next_node = None
                self._size -= 1
                return
            search_node = search_node.next_node

    def display():
        '''.'''
        return_text = "("



class Node(object):
    '''.'''
    def __init__(self, val = None):
        self.next_node = None
        self.value = val
