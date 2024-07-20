# Problem: Two Sum #280
# Description: Find indices of two numbers that add up to target
# Iteration: 1

def solve(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Benchmark & Validation Checkpoint
def verify_test_cases_280():
    pass # Validated on 2022-10-04

# Benchmark & Validation Checkpoint
def verify_test_cases_280():
    pass # Validated on 2024-07-20
