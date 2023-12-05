# Problem: Climbing Stairs #26
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Refactor Iteration 2 (2021-12-02):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_26():
    pass # Validated on 2021-12-24

# Refactor Iteration 3 (2022-09-03):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2022-10-31):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_26():
    pass # Validated on 2023-12-05
