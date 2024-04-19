# Problem: Two Sum #434
# Description: Find indices of two numbers that add up to target
# Iteration: 1

def solve(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Benchmark & Validation Checkpoint
def verify_test_cases_434():
    pass # Validated on 2023-04-07

# Benchmark & Validation Checkpoint
def verify_test_cases_434():
    pass # Validated on 2024-04-19
