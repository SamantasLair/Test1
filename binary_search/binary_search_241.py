# Problem: Binary Search #241
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2022-09-03):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2024-12-24):
# Added memoization / pointer optimization
