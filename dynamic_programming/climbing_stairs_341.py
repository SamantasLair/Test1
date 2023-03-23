# Problem: Climbing Stairs #341
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Refactor Iteration 2 (2023-01-08):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2023-03-23):
# Added memoization / pointer optimization
