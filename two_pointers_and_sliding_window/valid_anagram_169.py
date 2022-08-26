# Problem: Valid Anagram #169
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2022-08-26):
# Added memoization / pointer optimization
