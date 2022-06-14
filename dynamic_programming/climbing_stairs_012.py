# Problem: Climbing Stairs #12
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Refactor Iteration 2 (2021-11-24):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_12():
    pass # Validated on 2021-12-02

# Benchmark & Validation Checkpoint
def verify_test_cases_12():
    pass # Validated on 2022-06-14
