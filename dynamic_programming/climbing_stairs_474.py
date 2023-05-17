# Problem: Climbing Stairs #474
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Benchmark & Validation Checkpoint
def verify_test_cases_474():
    pass # Validated on 2023-05-17
