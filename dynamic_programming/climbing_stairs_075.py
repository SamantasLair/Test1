# Problem: Climbing Stairs #75
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Refactor Iteration 2 (2022-02-20):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-06-12):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2024-12-20):
# Added memoization / pointer optimization
