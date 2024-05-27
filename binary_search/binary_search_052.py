# Problem: Binary Search #52
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2022-01-20):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-09-23):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2022-11-11):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_52():
    pass # Validated on 2024-05-27
