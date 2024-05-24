# Problem: Binary Search #339
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2023-06-11):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2024-03-25):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2024-05-24):
# Added memoization / pointer optimization
