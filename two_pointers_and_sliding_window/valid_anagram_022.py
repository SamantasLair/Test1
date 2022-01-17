# Problem: Valid Anagram #22
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2021-12-09):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-01-18):
# Added memoization / pointer optimization
