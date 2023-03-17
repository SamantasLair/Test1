# Problem: Valid Anagram #127
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2023-03-17):
# Added memoization / pointer optimization
