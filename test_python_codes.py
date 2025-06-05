import pytest
from missing_number import find_missing_number_1
from missing_number import find_missing_number_2
from bracket_balance import is_balanced
from prime_gaps import is_prime, prime_gap

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

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(29) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-5) == False
    assert is_prime(97) == True

def test_prime_gap():
    assert prime_gap(10, 60) == (53, 59)
    assert prime_gap(1, 11) == (7, 11)
    assert prime_gap(20, 30) == (23, 29)
    
    with pytest.raises(ValueError):
        prime_gap(0, 1)  # No primes in this range
    with pytest.raises(ValueError):
        prime_gap(2, 2)  # No primes in this range
    with pytest.raises(ValueError):
        prime_gap(4, 4)  # No primes in this range
    with pytest.raises(ValueError):
        prime_gap(-10, -1)  # No primes in this range

if __name__ == '__main__':
    pytest.main(['-v', __file__])
    