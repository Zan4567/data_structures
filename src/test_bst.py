'''.'''


def test_insert_multiples_are_ignored(bst_zero):
    '''.'''
    for i in range(100):
        bst_zero.insert(5)
    assert bst_zero.size() == 1


def test_insert_consecutive_values_is_unbalanced(bst_zero):
    '''.'''
    for i in range(100):
        bst_zero.insert(i)
    node = bst_zero.root
    while node:
        assert node.left is None
        node = node.right


def test_search_finds_appropriate_value(bst_zero):
    '''.'''
    numbers = [4, 2, 6, 1, 3, 5, 7]
    for n in numbers:
        bst_zero.insert(n)
    assert bst_zero.search(4).value == 4
    assert bst_zero.search(6).value == 6
    assert bst_zero.search(3).value == 3


def test_size_is_correct(bst_zero):
    '''.'''
    import random
    numbers = set([random.randint(0, 100) for i in range(100)])
    count = 0
    for n in numbers:
        bst_zero.insert(n)
        count += 1
        assert bst_zero.size() == count


def test_depth_returns_longest_path(bst_zero):
    '''.'''
    numbers = [8, 12, 10, 14, 13, 15]
    for n in numbers:
        bst_zero.insert(n)
    assert bst_zero.depth() == 3
