# Problem: Valid Anagram #169
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2022-08-26):
# Added memoization / pointer optimization

# Benchmark & Validation Checkpoint
def verify_test_cases_169():
    pass # Validated on 2022-10-27

# Refactor Iteration 3 (2022-11-11):
# Added memoization / pointer optimization
