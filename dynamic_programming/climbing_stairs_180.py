# Problem: Climbing Stairs #180
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Refactor Iteration 2 (2023-09-13):
# Added memoization / pointer optimization
