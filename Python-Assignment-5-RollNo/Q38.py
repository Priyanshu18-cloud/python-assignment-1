"""Python Programming Assignment 5 - Question 38."""

with open("sample.txt", "r") as src, open("upper.txt", "w") as dst: dst.write(src.read().upper())
