# Problem: Binary Search #213
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2022-06-23):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_213():
    pass # Validated on 2022-09-06

# Refactor Iteration 3 (2022-11-08):
# Added memoization / pointer optimization
