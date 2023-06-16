# Problem: Valid Anagram #155
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2022-11-17):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2023-06-16):
# Added memoization / pointer optimization
