"""Tests for the linked list"""

import pytest


def test_node_has_attributes():
    """A node object must have a.value and next attribute."""
    from linked_list import Node
    n = Node(1)
    assert hasattr(n, 'value')
    assert hasattr(n, 'next_node')


def test_linked_list_had_head():
    """A new linked list should have a head."""
    from linked_list import Linked_List
    l = Linked_List()
    assert l.head is None


def test_linked_list_push_adds_new_item():
    """Linded List push method should add a new item to the list"""
    from linked_list import Linked_List
    l = Linked_List()
    l.push('val')
    assert l.head.value == 'val'


def test_linked_list_push_two_last_value_is_head():
    from linked_list import Linked_List
    l = Linked_List()
    l.push('val')
    l.push('val2')
    assert l.head.value == 'val2'


def test_linked_list_push_moves_old_head_to_new_heads_next():
    from linked_list import Linked_List
    l = Linked_List()
    l.push('val')
    l.push('val2')
    assert l.head.next_node.value == 'val'


def test_linked_list_pop_removes_head_and_returns_value():
    """."""
    from linked_list import Linked_List
    l = Linked_List()
    l.push('potato')
    popped = l.pop()
    assert popped is 'potato'


def test_linked_list_returns_head_value():
    """."""
    from linked_list import Linked_List
    l = Linked_List()
    l.push('potato')
    assert l.pop() == 'potato'


def test_linked_list_pop_shits_head_properly():
    """."""
    from linked_list import Linked_List
    l = Linked_List()
    l.push('potato')
    l.push('cabbage')
    l.pop()
    assert l.head.value == 'potato'


def test_linked_list_pop_empty_raises_exception():
    """."""
    from linked_list import Linked_List
    l = Linked_List()
    with pytest.raises(IndexError):
        l.pop()


def test_linked_list_size_returns_length():
    """."""
    from linked_list import Linked_List
    l = Linked_List()
    assert l.size() == 0


@pytest.mark.parametrize('n', range(10))
def test_linked_list_size_returns_length2(n):
    """."""
    from linked_list import Linked_List
    l = Linked_List()
    for i in range(n):
        l.push(i)
    assert l.size() == n


@pytest.mark.parametrize('n', range(10))
def test_linked_list_can_use_len_function(n):
    """."""
    from linked_list import Linked_List
    l = Linked_List()
    for i in range(n):
        l.push(i)
    assert len(l) == n


def test_linked_list_search_empty_returns_none():
    """."""
    from linked_list import Linked_List
    l = Linked_List()
    assert l.search(0) is None


def test_linked_list_search_with_one_node_returns_node():
    """."""
    from linked_list import Linked_List
    l = Linked_List()
    l.push(1)
    assert l.search(1) == l.head


def test_linked_list_search_with_one_node_bad_search():
    from linked_list import Linked_List
    l = Linked_List()
    l.push(1)
    assert l.search(0) is None


@pytest.mark.parametrize('n', range(1, 10))
def test_linked_list_search_in_many_returns_proper_node(n):
    """."""
    from linked_list import Linked_List
    from random import randint
    l = Linked_List()
    for i in range(1, n + 1):
        l.push(i)
    search_me = randint(1, n)
    assert l.search(search_me).value == search_me


def test_linked_list_takes_iterable_and_has_values():
    """."""
    from linked_list import Linked_List
    a_list = [5, 2, 9, 0, 1]
    l = Linked_List(a_list)
    for item in a_list:
        assert l.search(item).value == item


def test_linked_list_can_remove_value():
    from linked_list import Linked_List
    l = Linked_List()
    for i in range(10):
        l.push(i)
    l.remove(l.search(6))
    assert not l.search(6)


def test_linked_list_display_method_displays_correctly():
    from linked_list import Linked_List
    l = Linked_List(['potato', 'cabbage', 'gruel'])
    assert l.display() == "(gruel, cabbage, potato)"
