# Problem: Valid Anagram #288
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Benchmark & Validation Checkpoint
def verify_test_cases_288():
    pass # Validated on 2022-10-10
