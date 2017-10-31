import pytest


@pytest.fixture
def deque_no_nodes():
    from deque import Deque
    new_deque = Deque()
    return new_deque


@pytest.fixture
def deque_append_one():
    from deque import Deque
    d = Deque()
    d.appendleft('a')
    return d


@pytest.fixture
def deque_append_two():
    from deque import Deque
    d = Deque()
    d.appendleft('a')
    d.appendleft('b')
    return d
