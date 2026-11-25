"""Python Programming Assignment 5 - Question 24."""

with open("sample.txt", "r+") as f:
    old = f.read()
    f.seek(0)
    f.write("Updated: " + old)
