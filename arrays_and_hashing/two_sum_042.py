# Problem: Two Sum #42
# Description: Find indices of two numbers that add up to target
# Iteration: 1

def solve(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Refactor Iteration 2 (2022-02-22):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2023-03-30):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2024-03-18):
# Added memoization / pointer optimization
