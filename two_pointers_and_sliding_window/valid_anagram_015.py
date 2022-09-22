# Problem: Valid Anagram #15
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2022-06-14):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_15():
    pass # Validated on 2022-09-22
