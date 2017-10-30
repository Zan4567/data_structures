import pytest


@pytest.fixture
def dll_no_nodes():
    from double_linked_list import DoublyLinkedList
    return DoublyLinkedList()


@pytest.fixture
def dll_three_nodes():
    from double_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.push('sugar glider')
    dll.push('dog')
    dll.push('cat')
    return dll
