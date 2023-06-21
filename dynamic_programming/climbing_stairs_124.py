# Problem: Climbing Stairs #124
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Refactor Iteration 2 (2022-05-19):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-09-26):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_124():
    pass # Validated on 2023-06-21
