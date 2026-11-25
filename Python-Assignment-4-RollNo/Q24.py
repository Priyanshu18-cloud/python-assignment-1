"""Python Programming Assignment 4 - Question 24."""

def count_vowels(s): return sum(ch.lower() in "aeiou" for ch in s)
print(count_vowels("Education"))
