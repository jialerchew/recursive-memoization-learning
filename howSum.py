import time

"""
This function that checks if a given integer can be added up by a given list of smaller/equal integers.
If there is any possible combination, return any one of them. If there is no combination, return null.

Parameters:
    targetSum   : Given integer that needs to be checked
    numbers     : A list of numbers that can be used to add up to 'targetSum'

Returns:
    [array]     : An array of numbers that add up to exactly 'targetSum'. If no possible combination, return null
"""


def howSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None 

    for n in numbers:
        remainder = targetSum - n
        remainder_howSum = howSum(remainder, numbers)
        if remainder_howSum is not None: return [*remainder_howSum, n]

    return None

"""
This is the same function as the howSum function above, but with an additional parameter 'memo', which is a dictionary
that stores the output of the recursive function that it has calculated before.

Parameters:
    targetSum   : Given integer that needs to be checked
    numbers     : A list of numbers that can be used to add up to 'targetSum'
    memo        : A dict that stores all historical 'targetSum' that it has evaluated before through the recursion

Returns:
    [array]     : An array of numbers that add up to exactly 'targetSum'. If no possible combination, return null
"""

def howSumMemo(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None 

    for n in numbers:
        remainder = targetSum - n
        remainder_howSum = howSumMemo(remainder, numbers, memo)
        if remainder_howSum is not None:
            memo[targetSum] = [*remainder_howSum, n]
            return memo[targetSum]

    memo[targetSum] = None
    return None

"""
Below are some test cases to compare the execution time between memoized versus non-memoized recursive functions
"""
targetSum = 7
numbers = [2,3]
print("Sample 1: targetSum = {}, numbers = {}".format(targetSum,numbers))
print("## Non-memoized ##")
start = time.perf_counter()
print(howSum(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start))          # 
print("#### Memoized ####")
start = time.perf_counter()
print(howSumMemo(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start) + "\n")


targetSum = 167
numbers = [6,7,3,4]
print("Sample 2: targetSum = {}, numbers = {}".format(targetSum,numbers))
print("## Non-memoized ##")
start = time.perf_counter()
print(howSum(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start))
print("#### Memoized ####")
start = time.perf_counter()
print(howSumMemo(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start) + "\n")

targetSum = 250
numbers = [7,14]
print("Sample 3: targetSum = {}, numbers = {}".format(targetSum,numbers))
print("## Non-memoized ##")
start = time.perf_counter()
print(howSum(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start))
print("#### Memoized ####")
start = time.perf_counter()
print(howSumMemo(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start) + "\n")

"""
Console output:

Sample 1: targetSum = 7, numbers = [2, 3]
## Non-memoized ##
[3, 2, 2]
Time taken: 0.000020
#### Memoized ####
[3, 2, 2]
Time taken: 0.000020

Sample 2: targetSum = 167, numbers = [6, 7, 3, 4]
## Non-memoized ##
[4, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
Time taken: 0.000042
#### Memoized ####
[3, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
Time taken: 0.000047

Sample 3: targetSum = 250, numbers = [7, 14]
## Non-memoized ##
None
Time taken: 8.551811
#### Memoized ####
[3, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
Time taken: 0.000027

"""