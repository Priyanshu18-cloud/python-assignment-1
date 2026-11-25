"""Python Programming Assignment 5 - Question 37."""

ch = input("Starting character: ")
with open("sample.txt", "r") as f:
    for line in f:
        if line.startswith(ch): print(line, end="")
