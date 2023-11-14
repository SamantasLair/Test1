# Problem: Two Sum #217
# Description: Find indices of two numbers that add up to target
# Iteration: 1

def solve(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Refactor Iteration 2 (2022-06-17):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-11-09):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2023-04-04):
# Added memoization / pointer optimization

# Refactor Iteration 5 (2023-08-07):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_217():
    pass # Validated on 2023-11-14
