# Problem: Climbing Stairs #509
# Description: Calculate distinct ways to climb n steps
# Iteration: 1

def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)


# Refactor Iteration 2 (2024-09-02):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2024-11-20):
# Added memoization / pointer optimization
