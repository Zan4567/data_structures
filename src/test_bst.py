'''Tests for the binary search tree.'''


def test_initialize():
    '''Test of initialization with an iterator.'''
    import bst
    tree = bst.BinarySearchTree([3, 2, 5, 4, 7])
    assert tree.size() == 5


def test_insert_multiples_are_ignored(bst_zero):
    '''Test that duplicate values are ignored.'''
    for i in range(100):
        bst_zero.insert(5)
    assert bst_zero.size() == 1


def test_insert_consecutive_values_is_unbalanced(bst_zero):
    '''Test that adding numbers in order results in an unbalanced tree.'''
    for i in range(100):
        bst_zero.insert(i)
    node = bst_zero.root
    while node:
        assert node.left is None
        node = node.right


def test_search_empty_tree(bst_zero):
    '''Test that searching an empty tree returns None'''
    assert bst_zero.search(1) is None


def test_search_finds_appropriate_value(bst_zero):
    '''Test of the search function.'''
    numbers = [4, 2, 6, 1, 3, 5, 7]
    for n in numbers:
        bst_zero.insert(n)
    assert bst_zero.search(4).value == 4
    assert bst_zero.search(6).value == 6
    assert bst_zero.search(3).value == 3


def test_size_is_correct(bst_zero):
    '''Test of the size function.'''
    import random
    numbers = set([random.randint(0, 100) for i in range(100)])
    count = 0
    for n in numbers:
        bst_zero.insert(n)
        count += 1
        assert bst_zero.size() == count


def test_len(bst_zero):
    '''copy of above test with len'''
    import random
    numbers = set([random.randint(0, 100) for i in range(100)])
    count = 0
    for n in numbers:
        bst_zero.insert(n)
        count += 1
        assert len(bst_zero) == count


def test_depth_returns_longest_path(bst_zero):
    '''Test that depth returns depth of the longest branch.'''
    numbers = [8, 12, 10, 14, 9, 11]
    for n in numbers:
        bst_zero.insert(n)
    assert bst_zero.depth() == 3


def test_contains(bst_zero):
    '''Test of the contains function.'''
    numbers = [30, 15, 45, 4, 19, 40, 90]
    not_numbers = [1, 56, 12, 80]
    for i in numbers:
        bst_zero.insert(i)
    for i in numbers:
        assert bst_zero.contains(i)
    for i in not_numbers:
        assert not bst_zero.contains(i)


def test_balance_of_empty_tree(bst_zero):
    '''assert that the balance of an empty tree is 0'''
    assert bst_zero.balance() == 0


def test_balanced_tree(bst_zero):
    '''Test that the balance of a balanced tree is 0.'''
    numbers = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5,
               7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    for n in numbers:
        bst_zero.insert(n)

    assert bst_zero.balance() == 0


def test_unbalanced_tree(bst_zero):
    '''Test that an unbalanced tree returns the correct value.'''
    numbers = [8, 12, 10, 14, 9, 11]
    for n in numbers:
        bst_zero.insert(n)
    assert bst_zero.balance() == 3
