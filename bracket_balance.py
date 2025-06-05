def is_balanced(s: str) -> bool:
    '''Check if the string has balanced parentheses.'''
    stack = []
    matching = {'(':')', '{':'}', '[':']'}
    for char in s:
        if char in matching:
            stack.append(char)
        elif char in matching.values():
            if not stack or matching[stack.pop()] != char:
                return False
    return not stack

if __name__=='__main__': # Code under this block will not run if you import the file elsewhere.
    print(is_balanced("({[]})"))
    print(is_balanced(']['))
    print(is_balanced('()'))

