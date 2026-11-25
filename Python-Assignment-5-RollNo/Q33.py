"""Python Programming Assignment 5 - Question 33."""

with open("sample.txt", "r") as f: text = f.read()
print("Digits:", sum(c.isdigit() for c in text))
print("Special:", sum(not c.isalnum() and not c.isspace() for c in text))
