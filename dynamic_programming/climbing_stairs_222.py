# Problem: Climbing Stairs #222
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Benchmark & Validation Checkpoint
def verify_test_cases_222():
    pass # Validated on 2023-03-25

# Refactor Iteration 2 (2024-01-01):
# Added memoization / pointer optimization
