# Problem: Valid Anagram #477
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2023-06-08):
# Added memoization / pointer optimization
