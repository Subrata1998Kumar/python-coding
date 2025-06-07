import pytest
from missing_number import find_missing_number_1
from missing_number import find_missing_number_2
from bracket_balance import is_balanced
from prime_gaps import is_prime, prime_gap
from palindrome_with_clean import clean_string, palindrome_check, palindrome_check_with_for_loop
from longest_valid_parantheses import longest_vaild_parentheses, longest_vaild_parentheses1

def test_find_missing_number_1():
    '''Test the find_missing_number_1 function to ensure it finds the missing number correctly.'''
    """Test cases for find_missing_number_1 function."""
    assert find_missing_number_1([1, 2, 4, 5]) == 3
    assert find_missing_number_1([3, 7, 1, 2, 8, 4, 5]) == 6
    assert find_missing_number_1([1]) == 2
    assert find_missing_number_1([]) == 1
    assert find_missing_number_1([2]) == 1
    assert find_missing_number_1([1, 3]) == 2

def test_find_missing_number_2():
    '''Test the find_missing_number_2 function to ensure it finds the missing number correctly.'''
    assert find_missing_number_2([1, 2, 4, 5]) == 3
    assert find_missing_number_2([3, 7, 1, 2, 8, 4, 5]) == 6
    assert find_missing_number_2([1]) == 2
    assert find_missing_number_2([]) == 1
    assert find_missing_number_2([2]) == 1
    assert find_missing_number_2([1, 3]) == 2

def test_is_balanced():
    '''Test the is_balanced function to ensure it correctly identifies balanced parentheses.'''
    assert is_balanced('()') == True
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
    '''Test the is_prime function to ensure it correctly identifies prime numbers.'''
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
    '''Test the prime_gap function to ensure it finds the largest gap between consecutive primes.'''
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

def test_string_clean():
    '''Test the clean_string function to ensure it removes non-alphanumeric characters.'''
    assert clean_string("Hello, World!") == "HelloWorld"
    assert clean_string("1234!@#$") == "1234"
    assert clean_string("") == ""
    assert clean_string('''_-'H'ell`o`,"World"''') == "HelloWorld"

def test_palindrome_check():
    '''Test the palindrome_check function to ensure it correctly identifies palindromes.'''
    assert palindrome_check("A man, a plan, a canal: Panama") == True
    assert palindrome_check("No 'x' in Nixon") == True
    assert palindrome_check("Was it a car or a cat I saw?") == True
    assert palindrome_check("Hello, World!") == False
    assert palindrome_check("12321") == True
    assert palindrome_check("12345") == False

def test_palindrome_check_with_for_loop():
    '''Test the palindrome_check_with_for_loop function to ensure it correctly identifies palindromes.'''
    assert palindrome_check_with_for_loop("A man, a plan, a canal: Panama") == True
    assert palindrome_check_with_for_loop("No 'x' in Nixon") == True
    assert palindrome_check_with_for_loop("Was it a car or a cat I saw?") == True
    assert palindrome_check_with_for_loop("Hello, World!") == False
    assert palindrome_check_with_for_loop("12321") == True
    assert palindrome_check_with_for_loop("12345") == False

def test_longest_valid_parantheses():
    '''Test the longest_vaild_parantheses function to ensure it finds the longest valid parentheses substring.'''
    assert longest_vaild_parentheses('(((())))') == 8
    assert longest_vaild_parentheses(")))))))((()))") == 6
    assert longest_vaild_parentheses('()()()') == 6
    assert longest_vaild_parentheses('(()') == 2
    assert longest_vaild_parentheses(')()())') == 4
    assert longest_vaild_parentheses('') == 0
    assert longest_vaild_parentheses('((((()))))') == 10

def test_longest_valid_parantheses1():
    '''Test the longest_vaild_parentheses1 function to ensure it finds the longest valid parentheses substring.'''
    assert longest_vaild_parentheses1('(((())))') == 8
    assert longest_vaild_parentheses1(")))))))((()))") == 6
    assert longest_vaild_parentheses1('()()()') == 2
    assert longest_vaild_parentheses1('(()') == 2
    assert longest_vaild_parentheses1(')()())') == 2
    assert longest_vaild_parentheses1('') == 0
    assert longest_vaild_parentheses1('((((()))))') == 10

if __name__ == '__main__':
    pytest.main(['-v', __file__])
    