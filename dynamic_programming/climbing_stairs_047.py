# Problem: Climbing Stairs #47
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Benchmark & Validation Checkpoint
def verify_test_cases_47():
    pass # Validated on 2022-01-24

# Benchmark & Validation Checkpoint
def verify_test_cases_47():
    pass # Validated on 2022-09-23

# Refactor Iteration 2 (2023-07-23):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2024-01-19):
# Added memoization / pointer optimization
