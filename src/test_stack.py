"""Test the Stack"""

import pytest


def stack_fixture():
    """."""
    from stack import Stack
    return Stack()


def stack_push_once():
    """Create stack object with one node"""
    from stack import Stack
    s = Stack()
    s.stack.push(5)
    return s


def stack_push_twice():
    """Create stack object with two  nodes"""
    from stack import Stack
    s = Stack()
    s.stack.push(5)
    s.stack.push(10)
    return s


def stack_push_three():
    """Create stack object with three  nodes"""
    from stack import Stack
    s = Stack()
    s.stack.push(5)
    s.stack.push(10)
    s.stack.push(20)
    return s


PUSH_TABLE = [
    (stack_fixture(), 0),
    (stack_push_once(), 1),
    (stack_push_twice(), 2)
]


def test_cant_pop_empty_stack():
    """Test that popping empty list returns IndexError"""
    with pytest.raises(IndexError, match='Empty list, nothing to pop'):
        stack_fixture().stack.pop()


def test_pop_returns_last_in():
    """Test that last pushed node value is returned when popped"""
    s = stack_push_once()
    head = s.stack.head
    popped = s.stack.pop()
    assert head.value == popped


def test_push_pushes_value_to_head():
    """Check that value pushed to head actually becomes head's value"""
    assert stack_push_once().stack.pop() == 5


def test_dunder_length_returns_type_int():
    """Test length function on empty stack returns an int."""
    assert isinstance(stack_fixture().stack.__len__(), int)


@pytest.mark.parametrize('pushes, length', PUSH_TABLE)
def test_correct_lengths_after_pushing(pushes, length):
    """Test length of stack correct after push(es)"""
    assert pushes.stack.__len__() == length


def test_correct_lengths_after_popping():
    """Test length of stack correct after pop(s)"""
    s = stack_push_three()
    for i in range(s.stack.__len__()-1, -1):
        s.stack.pop()
        assert s.stack.__len__() == i


def test_push_twice_new_node_points_to_previous():
    """Test when 2 nodes pushed that 2nd node pushed points to first"""
    s = stack_push_twice()
    first_node_in = s.stack.head
    second_node_in = s.stack.head.next_node
    assert first_node_in.next_node == second_node_in



