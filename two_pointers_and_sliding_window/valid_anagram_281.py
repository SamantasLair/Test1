# Problem: Valid Anagram #281
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2023-12-19):
# Added memoization / pointer optimization
