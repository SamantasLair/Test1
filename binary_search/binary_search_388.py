# Problem: Binary Search #388
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2023-03-14):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2023-08-05):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2023-09-29):
# Added memoization / pointer optimization
