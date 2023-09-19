# Problem: Two Sum #588
# Description: Find indices of two numbers that add up to target
# Iteration: 1

def solve(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

