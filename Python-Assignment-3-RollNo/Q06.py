"""Python Programming Assignment 3 - Question 6."""

s = input("Enter string: ")
print("Uppercase:", sum(ch.isupper() for ch in s))
print("Lowercase:", sum(ch.islower() for ch in s))
