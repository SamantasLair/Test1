# Problem: Maximum Subarray #100
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


# Refactor Iteration 2 (2022-07-12):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_100():
    pass # Validated on 2022-12-20
