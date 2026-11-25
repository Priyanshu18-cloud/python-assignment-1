"""Python Programming Assignment 5 - Question 28."""

with open("sample.txt", "r") as f:
    f.seek(5)
    print("Position:", f.tell())
