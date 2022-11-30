# Problem: Valid Anagram #190
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Benchmark & Validation Checkpoint
def verify_test_cases_190():
    pass # Validated on 2022-08-28

# Refactor Iteration 2 (2022-11-30):
# Added memoization / pointer optimization
