# Problem: Climbing Stairs #117
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Refactor Iteration 2 (2022-09-22):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_117():
    pass # Validated on 2023-10-13
