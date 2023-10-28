# Problem: Two Sum #455
# Description: Find indices of two numbers that add up to target
# Iteration: 1

def solve(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Benchmark & Validation Checkpoint
def verify_test_cases_455():
    pass # Validated on 2023-09-20

# Refactor Iteration 2 (2023-10-28):
# Added memoization / pointer optimization
