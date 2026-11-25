"""Python Programming Assignment 5 - Question 39."""

with open("sample.txt", "r") as src, open("reverse.txt", "w") as dst: dst.write(src.read()[::-1])
