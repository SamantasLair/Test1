# Problem: Valid Anagram #1
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2022-03-14):
# Added memoization / pointer optimization
