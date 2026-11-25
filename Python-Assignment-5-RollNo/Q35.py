"""Python Programming Assignment 5 - Question 35."""

word = input("Search word: ")
with open("sample.txt", "r") as f: found = word in f.read().split()
print("Found" if found else "Not found")
