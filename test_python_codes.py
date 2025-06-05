import pytest
from missing_number import find_missing_number_1
from missing_number import find_missing_number_2
from bracket_balance import is_balanced

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

def test_is_balanced():
    assert is_balanced('({[]})') == True
    assert is_balanced('[') == False
    assert is_balanced(']') == False
    assert is_balanced('][') == False
    assert is_balanced('') == True
    assert is_balanced('([]{})') == True
    assert is_balanced('([)]') == False
    assert is_balanced('((()))') == True
    assert is_balanced('((())') == False
    assert is_balanced('{[()]}') == True
    assert is_balanced('{[(])}') == False
    assert is_balanced('no brackets') == True
    assert is_balanced('[' * 1000 + ']' * 1000) == True

if __name__ == '__main__':
    pytest.main(['-v', __file__])
    