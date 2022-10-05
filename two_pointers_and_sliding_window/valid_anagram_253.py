# Problem: Valid Anagram #253
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2022-10-05):
# Added memoization / pointer optimization
