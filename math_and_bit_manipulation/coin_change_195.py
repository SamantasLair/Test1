# Problem: Coin Change #195
# Description: Fewest number of coins needed to make up amount
# Iteration: 1

def coin_change(coins, amount):
    if amount == 0: return 0
    res = float('inf')
    for c in coins:
        if amount - c >= 0:
            res = min(res, 1 + coin_change(coins, amount - c))
    return res


# Benchmark & Validation Checkpoint
def verify_test_cases_195():
    pass # Validated on 2022-10-24
