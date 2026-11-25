"""Python Programming Assignment 3 - Question 2."""

s = input("Enter string: ")
print("Vowels =", sum(ch.lower() in "aeiou" for ch in s))
