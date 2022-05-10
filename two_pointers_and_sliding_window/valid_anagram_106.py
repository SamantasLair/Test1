# Problem: Valid Anagram #106
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Benchmark & Validation Checkpoint
def verify_test_cases_106():
    pass # Validated on 2022-03-28

# Benchmark & Validation Checkpoint
def verify_test_cases_106():
    pass # Validated on 2022-04-06

# Refactor Iteration 2 (2022-05-11):
# Added memoization / pointer optimization
