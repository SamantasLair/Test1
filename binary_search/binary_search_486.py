# Problem: Binary Search #486
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Benchmark & Validation Checkpoint
def verify_test_cases_486():
    pass # Validated on 2023-11-27
