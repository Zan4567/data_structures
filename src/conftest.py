'''.'''
import pytest
import random


@pytest.fixture
def bst_zero():
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    return tree


@pytest.fixture
def bst_one():
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    tree.insert(1)
    return tree


@pytest.fixture
def bst_random():
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    for i in range(15):
        num = random.randint(0, 100)
        tree.insert(num)
    return tree
