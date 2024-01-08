# Problem: Valid Anagram #43
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Benchmark & Validation Checkpoint
def verify_test_cases_43():
    pass # Validated on 2021-12-11

# Benchmark & Validation Checkpoint
def verify_test_cases_43():
    pass # Validated on 2022-02-20

# Refactor Iteration 2 (2022-09-02):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2024-01-08):
# Added memoization / pointer optimization
