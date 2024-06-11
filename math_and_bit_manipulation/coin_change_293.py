# Problem: Coin Change #293
# Description: Fewest number of coins needed to make up amount
# Iteration: 1

def coin_change(coins, amount):
    if amount == 0: return 0
    res = float('inf')
    for c in coins:
        if amount - c >= 0:
            res = min(res, 1 + coin_change(coins, amount - c))
    return res


# Refactor Iteration 2 (2023-02-11):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2024-06-11):
# Added memoization / pointer optimization
