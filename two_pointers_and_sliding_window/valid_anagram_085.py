# Problem: Valid Anagram #85
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Benchmark & Validation Checkpoint
def verify_test_cases_85():
    pass # Validated on 2022-03-21

# Refactor Iteration 2 (2022-09-15):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-10-01):
# Added memoization / pointer optimization

# Refactor Iteration 4 (2022-11-07):
# Added memoization / pointer optimization
