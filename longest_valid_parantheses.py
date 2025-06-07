def longest_vaild_parentheses(s: str) -> int:
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

def longest_vaild_parentheses1(s: str) -> bool:
    ''' Find logest valid parentheses'''
    stack = []
    max_len = 0
    for index, char in enumerate(s):
        if char == '(':
            stack.append(index)
        else:
            if len(stack) > 0:
                max_len = max(max_len, index+1-stack[-1])
                stack.pop()
    return max_len


if __name__ == '__main__': # This section of code will not run if we import this module elsewhere
    print(longest_vaild_parentheses('(((())))'))
    print(longest_vaild_parentheses(")))))))((()))"))
    print(longest_vaild_parentheses('()()()'))

    print("******* 1 **************")
    print(longest_vaild_parentheses1('(((())))'))
    print(longest_vaild_parentheses1(")))))))((()))"))
    print(longest_vaild_parentheses1('()()()'))
    
