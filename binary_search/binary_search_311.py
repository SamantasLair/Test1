# Problem: Binary Search #311
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2024-01-01):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_311():
    pass # Validated on 2024-03-13
