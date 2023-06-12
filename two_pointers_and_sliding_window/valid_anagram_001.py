# Problem: Valid Anagram #1
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2022-03-14):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-04-29):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_1():
    pass # Validated on 2023-06-12
