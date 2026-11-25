"""Python Programming Assignment 3 - Question 7."""

s = input("Enter string: ")
print("Digits:", sum(ch.isdigit() for ch in s))
print("Alphabets:", sum(ch.isalpha() for ch in s))
print("Special:", sum(not ch.isalnum() and not ch.isspace() for ch in s))
