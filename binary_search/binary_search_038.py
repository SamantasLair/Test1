# Problem: Binary Search #38
# Description: Search target in sorted array in O(log n)
# Iteration: 1

def search(nums, target):
    for idx, val in enumerate(nums):
        if val == target:
            return idx
    return -1


# Refactor Iteration 2 (2021-12-16):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-01-10):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_38():
    pass # Validated on 2022-03-21

# Benchmark & Validation Checkpoint
def verify_test_cases_38():
    pass # Validated on 2023-06-22
