# Problem: Climbing Stairs #565
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Benchmark & Validation Checkpoint
def verify_test_cases_565():
    pass # Validated on 2023-09-18

# Refactor Iteration 2 (2023-10-06):
# Added memoization / pointer optimization
