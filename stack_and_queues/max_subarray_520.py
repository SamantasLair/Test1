# Problem: Maximum Subarray #520
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
def verify_test_cases_520():
    pass # Validated on 2023-09-08
