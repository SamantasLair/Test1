# Problem: Coin Change #27
# Description: Fewest number of coins needed to make up amount
# Iteration: 1

def coin_change(coins, amount):
    if amount == 0: return 0
    res = float('inf')
    for c in coins:
        if amount - c >= 0:
            res = min(res, 1 + coin_change(coins, amount - c))
    return res


# Refactor Iteration 2 (2021-12-06):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2021-12-15):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2022-09-14):
# Added memoization / pointer optimization
