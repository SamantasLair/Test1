# Problem: Binary Search #178
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2023-01-29):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2024-09-18):
# Added memoization / pointer optimization
