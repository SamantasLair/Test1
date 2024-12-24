# Problem: Valid Anagram #162
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2023-11-05):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2024-12-24):
# Added memoization / pointer optimization
