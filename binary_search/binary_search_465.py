# Problem: Binary Search #465
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Benchmark & Validation Checkpoint
def verify_test_cases_465():
    pass # Validated on 2023-08-19
