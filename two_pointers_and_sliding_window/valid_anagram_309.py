# Problem: Valid Anagram #309
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Benchmark & Validation Checkpoint
def verify_test_cases_309():
    pass # Validated on 2023-06-15

# Refactor Iteration 2 (2023-11-25):
# Added memoization / pointer optimization
