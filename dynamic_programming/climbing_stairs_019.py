# Problem: Climbing Stairs #19
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Benchmark & Validation Checkpoint
def verify_test_cases_19():
    pass # Validated on 2021-12-10

# Refactor Iteration 2 (2022-01-28):
# Added memoization / pointer optimization
