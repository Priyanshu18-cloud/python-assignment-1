"""Python Programming Assignment 5 - Question 4."""

with open("sample.txt", "r") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()
