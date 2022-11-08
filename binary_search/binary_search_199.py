# Problem: Binary Search #199
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2022-06-09):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-11-08):
# Added memoization / pointer optimization
