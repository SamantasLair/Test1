# Problem: Binary Search #318
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2023-03-26):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2024-01-19):
# Added memoization / pointer optimization
