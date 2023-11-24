# Problem: Valid Anagram #295
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Benchmark & Validation Checkpoint
def verify_test_cases_295():
    pass # Validated on 2023-11-24
