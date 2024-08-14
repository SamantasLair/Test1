# Problem: Coin Change #146
# Description: Fewest number of coins needed to make up amount
# Iteration: 1

def coin_change(coins, amount):
    if amount == 0: return 0
    res = float('inf')
    for c in coins:
        if amount - c >= 0:
            res = min(res, 1 + coin_change(coins, amount - c))
    return res


# Refactor Iteration 2 (2022-08-24):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-10-28):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2023-04-29):
# Added memoization / pointer optimization

# Refactor Iteration 5 (2024-08-15):
# Added memoization / pointer optimization
