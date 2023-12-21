# Problem: Climbing Stairs #488
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Refactor Iteration 2 (2023-12-21):
# Added memoization / pointer optimization
