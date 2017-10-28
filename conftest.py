import pytest


@pytest.fixture
def queue_no_nodes():
    from que_ import Queue
    new_queue = Queue()
    return new_queue


@pytest.fixture
def queue_three_nodes():
    from que_ import Queue
    new_queue = Queue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    return new_queue
