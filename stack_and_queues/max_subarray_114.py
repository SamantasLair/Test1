# Problem: Maximum Subarray #114
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


# Refactor Iteration 2 (2022-04-30):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-05-04):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2023-03-10):
# Added memoization / pointer optimization
