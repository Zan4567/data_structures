"""."""

class Node(object):
    """."""
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    """."""
    def __init__(self):
        self.tail = None
        self.head = None
        self._size = 0

    def push(self, val):
        new_node = Node(val)
        if self._size == 0:
            self.list_begins(new_node)
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self._size += 1

    def append(self, val):
        new_node = Node(val)
        if self._size == 0:
            self.list_begins(new_node)
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self._size += 1

    def list_begins(self, node):
        self.tail = node
        self.head = node
        self._size += 1

    def pop_single_node(self):
        """pop when there is only one node in the list."""
        single_node = self.head
        self.head = None
        self.tail = None
        self._size -= 1
        return single_node.val

    def pop(self):
        if self._size == 0:
            raise IndexError("Empty list, nothing to pop")
        elif self._size == 1:
            return pop_single_node()
        the_head = self.head
        self.head = self.head.next
        self.head.prev = None
        self._size -= 1
        return the_head.val


    def shift(self):
        if self._size == 0:
            raise IndexError("Empty list, nothing to pop")
        elif self._size == 1:
            return pop_single_node()
        the_tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self._size -= 1
        return the_tail.val

    def remove(self, value):
        current = self.head
        while current:
            if current.val == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self._size -= 1
            current = current.next
        raise ValueError('Value not in list')


