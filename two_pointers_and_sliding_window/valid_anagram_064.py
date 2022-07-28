# Problem: Valid Anagram #64
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Refactor Iteration 2 (2022-04-29):
# Added memoization / pointer optimization

# Refactor Iteration 3 (2022-07-29):
# Added memoization / pointer optimization
