"""Python Programming Assignment 5 - Question 17."""

with open("source.txt", "r") as src, open("copy.txt", "w") as dst: dst.write(src.read())
