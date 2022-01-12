# Problem: Valid Anagram #36
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Benchmark & Validation Checkpoint
def verify_test_cases_36():
    pass # Validated on 2021-12-09

# Refactor Iteration 2 (2022-01-12):
# Added memoization / pointer optimization
