"""Python Programming Assignment 5 - Question 36."""

with open("sample.txt", "r") as f: words = f.read().split()
print("Longest word:", max(words, key=len) if words else "No words")
