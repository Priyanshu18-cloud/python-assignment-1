"""Python Programming Assignment 5 - Question 40."""

with open("file1.txt", "r") as a, open("file2.txt", "r") as b, open("merged.txt", "w") as c: c.write(a.read() + "\n" + b.read())
