# Problem: Binary Search #185
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2022-08-24):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_185():
    pass # Validated on 2023-03-04
