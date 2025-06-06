def clean_string(s: str) -> str:
    '''Remove all non alphanumeric characters from the string'''
    return ''.join(char for char in s if char.isalnum())

def palindrome_check(s: str) -> bool:
    ''' Check if the string is a palindrome'''
    clean_text = clean_string(s).lower()
    return clean_text == clean_text[::-1]

def palindrome_check_with_for_loop(s: str) -> bool:
    ''' Check if the string is a palindrome'''
    clean = clean_string(s).lower()
    n = len(clean)
    for i in range(n//2):
        if clean[i] != clean[n-1-i]:
            return False
    return True

if __name__ == '__main__': # This section of code will not run if we import the file elsewhere
    print(palindrome_check("A man, a plan, a canal: Panama"))
    print(palindrome_check_with_for_loop("A man, a plan, a canal: Panama"))