import time

"""
This function that checks if a given integer can be added up by a given list of smaller/equal integers.
If there is any possible combination, return any of the shortest combinations. If there is no combination, return null.

Parameters:
    targetSum   : Given integer that needs to be checked
    numbers     : A list of numbers that can be used to add up to 'targetSum'

Returns:
    [array]     : The shortest combination of numbers that add up to exactly 'targetSum'. If no possible combination, return null
"""


def bestSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None 

    shortestCombination = None

    for n in numbers:
        remainder = targetSum - n
        remainder_bestSum = bestSum(remainder, numbers)
        if remainder_bestSum is not None:
            combination = [*remainder_bestSum, n]
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    return shortestCombination

"""
This is the same function as the bestSum function above, but with an additional parameter 'memo', which is a dictionary
that stores the output of the recursive function that it has calculated before.

Parameters:
    targetSum   : Given integer that needs to be checked
    numbers     : A list of numbers that can be used to add up to 'targetSum'
    memo        : A dict that stores all historical 'targetSum' that it has evaluated before through the recursion

Returns:
    [array]     : An array of numbers that add up to exactly 'targetSum'. If no possible combination, return null
"""

def bestSumMemo(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None 

    shortestCombination = None

    for n in numbers:
        remainder = targetSum - n
        remainder_bestSum = bestSumMemo(remainder, numbers, memo)
        if remainder_bestSum is not None:
            combination = [*remainder_bestSum, n]
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return memo[targetSum]

"""
Below are some test cases to compare the execution time between memoized versus non-memoized recursive functions
"""
targetSum = 7
numbers = [5,3,4,7]
print("Sample 1: targetSum = {}, numbers = {}".format(targetSum,numbers))
print("## Non-memoized ##")
start = time.perf_counter()
print(bestSum(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start))          # 
print("#### Memoized ####")
start = time.perf_counter()
print(bestSumMemo(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start) + "\n")


targetSum = 8
numbers = [2,3,5]
print("Sample 2: targetSum = {}, numbers = {}".format(targetSum,numbers))
print("## Non-memoized ##")
start = time.perf_counter()
print(bestSum(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start))
print("#### Memoized ####")
start = time.perf_counter()
print(bestSumMemo(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start) + "\n")

targetSum = 8
numbers = [1,4,5]
print("Sample 3: targetSum = {}, numbers = {}".format(targetSum,numbers))
print("## Non-memoized ##")
start = time.perf_counter()
print(bestSum(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start))
print("#### Memoized ####")
start = time.perf_counter()
print(bestSumMemo(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start) + "\n")

targetSum = 70
numbers = [2,5,25]
print("Sample 4: targetSum = {}, numbers = {}".format(targetSum,numbers))
print("## Non-memoized ##")
start = time.perf_counter()
print(bestSum(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start))
print("#### Memoized ####")
start = time.perf_counter()
print(bestSumMemo(targetSum, numbers))
end = time.perf_counter()
print("Time taken: " + "{:.6f}".format(end-start) + "\n")

"""
Console output:

Sample 1: targetSum = 7, numbers = [5, 3, 4, 7]
## Non-memoized ##
[7]
Time taken: 0.000033
#### Memoized ####
[7]
Time taken: 0.000043

Sample 2: targetSum = 8, numbers = [2, 3, 5]
## Non-memoized ##
[5, 3]
Time taken: 0.000043
#### Memoized ####
[5, 3]
Time taken: 0.000049

Sample 3: targetSum = 8, numbers = [1, 4, 5]
## Non-memoized ##
[4, 4]
Time taken: 0.000089
#### Memoized ####
[5, 3]
Time taken: 0.000017

Sample 4: targetSum = 70, numbers = [2, 5, 25]
## Non-memoized ##
[25, 25, 5, 5, 5, 5]
Time taken: 2.300834
#### Memoized ####
[25, 25, 5, 5, 5, 5]
Time taken: 0.000089

"""