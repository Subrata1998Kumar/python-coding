import pytest
from missing_number import find_missing_number_1
from missing_number import find_missing_number_2

def test_find_missing_number_1():
    assert find_missing_number_1([1, 2, 4, 5]) == 3
    assert find_missing_number_1([3, 7, 1, 2, 8, 4, 5]) == 6
    assert find_missing_number_1([1]) == 2
    assert find_missing_number_1([]) == 1
    assert find_missing_number_1([2]) == 1
    assert find_missing_number_1([1, 3]) == 2

def test_find_missing_number_2():
    assert find_missing_number_2([1, 2, 4, 5]) == 3
    assert find_missing_number_2([3, 7, 1, 2, 8, 4, 5]) == 6
    assert find_missing_number_2([1]) == 2
    assert find_missing_number_2([]) == 1
    assert find_missing_number_2([2]) == 1
    assert find_missing_number_2([1, 3]) == 2


if __name__ == '__main__':
    pytest.main(['-v', __file__])
    