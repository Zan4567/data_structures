class Node(object):

    def __init__(self, value=None):
        self.next_node = None
        self.value = value


class Queue(object):

    def __init__(self):
        self._size = 0
        self.front = None
        self.back = None

    def enqueue(self, value):
        '''add a node to the end of the queue with given value'''
        new_node = Node(value)
        if self.back is None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next_node = new_node
            self.back = new_node
        self._size += 1

    def dequeue(self):
        '''take node from front of the queue and return its value'''
        if self.front is None:
            raise IndexError
        front_node = self.front
        self.front = self.front.next_node
        if front_node is self.back:
            self.back = None
        self._size -= 1
        return front_node.value

    def peek(self):
        '''look at the value of the node at the front of the queue'''
        if self.front is None:
            return None
        return self.front.value

    def size(self):
        '''return the number of nodes in the queue'''
        return self._size

    def __len__(self):
        '''return the number of nodes in the queue. Functionally identical to
        size()'''
        return self._size
