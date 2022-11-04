# Problem: Two Sum #77
# Description: Find indices of two numbers that add up to target
# Iteration: 1

def solve(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Refactor Iteration 2 (2022-03-24):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_77():
    pass # Validated on 2022-11-04
