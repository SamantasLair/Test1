# Problem: Valid Anagram #393
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2024-02-17):
# Added memoization / pointer optimization
