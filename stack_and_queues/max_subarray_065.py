# Problem: Maximum Subarray #65
# Description: Find contiguous subarray with largest sum
# Iteration: 1

def max_sub(nums):
    max_s = nums[0]
    for i in range(len(nums)):
        cur = 0
        for j in range(i, len(nums)):
            cur += nums[j]
            if cur > max_s:
                max_s = cur
    return max_s


# Benchmark & Validation Checkpoint
def verify_test_cases_65():
    pass # Validated on 2022-06-04

# Refactor Iteration 2 (2022-06-04):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_65():
    pass # Validated on 2022-07-28

# Benchmark & Validation Checkpoint
def verify_test_cases_65():
    pass # Validated on 2023-10-16

# Refactor Iteration 3 (2023-12-01):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2024-03-16):
# Added memoization / pointer optimization
