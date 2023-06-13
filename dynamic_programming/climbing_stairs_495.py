# Problem: Climbing Stairs #495
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Refactor Iteration 2 (2023-06-13):
# Added memoization / pointer optimization
