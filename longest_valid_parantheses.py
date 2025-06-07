def longest_vaild_parantheses(s: str) -> int:
    ''' Find the length of the longest valid parentheses substring.'''
    stack = [-1]
    max_gap = 0
    for index, char in enumerate(s):
        if char == '(':
            stack.append(index)
        else:
            stack.pop()
            if not stack:
                stack.append(index)
            else:
                max_gap = max(max_gap, index - stack[-1])
    return max_gap

if __name__ == '__main__': # This section of code will not run if we import this module elsewhere
    print(longest_vaild_parantheses('(((())))'))
    print(longest_vaild_parantheses(")))))))((()))"))
    print(longest_vaild_parantheses('()()()'))
    
