"""Python Programming Assignment 5 - Question 9."""

word = input("Search word: ")
with open("sample.txt", "r") as f:
    for line in f:
        if word in line: print(line, end="")
