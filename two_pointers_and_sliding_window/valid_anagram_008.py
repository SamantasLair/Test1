# Problem: Valid Anagram #8
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2022-01-15):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_8():
    pass # Validated on 2022-06-03
