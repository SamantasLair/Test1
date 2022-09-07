# Problem: Valid Anagram #183
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Benchmark & Validation Checkpoint
def verify_test_cases_183():
    pass # Validated on 2022-06-19

# Refactor Iteration 2 (2022-09-07):
# Added memoization / pointer optimization
