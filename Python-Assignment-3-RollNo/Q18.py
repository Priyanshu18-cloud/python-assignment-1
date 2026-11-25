"""Python Programming Assignment 3 - Question 18."""

s = input("Enter sentence: ")
words = s.split()
print(max(words, key=len) if words else "No words")
