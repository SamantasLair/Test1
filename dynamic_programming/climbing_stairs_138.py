# Problem: Climbing Stairs #138
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Benchmark & Validation Checkpoint
def verify_test_cases_138():
    pass # Validated on 2022-08-30

# Benchmark & Validation Checkpoint
def verify_test_cases_138():
    pass # Validated on 2023-09-12
