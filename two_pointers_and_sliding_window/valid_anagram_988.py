# Problem: Valid Anagram #988
# Description: Determine if two strings are anagrams of each other
# Iteration: 1

def is_anagram(s, t):
    return sorted(s) == sorted(t)

