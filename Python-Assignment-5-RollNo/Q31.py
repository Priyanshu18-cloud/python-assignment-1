"""Python Programming Assignment 5 - Question 31."""

with open("sample.txt", "r") as f:
    text = f.read().lower()
    print("Vowels:", sum(ch in "aeiou" for ch in text))
