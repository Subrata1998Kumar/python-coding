def find_missing_number_1(nums: list[int]) -> int:
    '''miss_num = (1+2+3+...+n) - sum(nums)'''
    n = len(nums) +1
    # Calculate the total sum of numbers from 1 to n.
    total_sum = n * (n+1) // 2
    # Find the missing numer from the list.
    return total_sum - sum(nums)

def find_missing_number_2(nums: list[int]) -> int:
    '''Using for to find the missing number'''
    n = len(nums) + 1
    
    for i in range(1, n + 1):
        if i not in nums:
            return i



if __name__ == '__main__': # Code under this block will not run if you import the file elsewhere.
    nums = [1, 2, 4, 5]
    print(f'Missing number is: {find_missing_number_1(nums)}')  
    print(f'Missing number is: {find_missing_number_2(nums)}')  
    nums = [3, 7, 1, 2, 8, 4, 5]
    print(f'Missing number is: {find_missing_number_1(nums)}') 
    print(f'Missing number is: {find_missing_number_2(nums)}') 