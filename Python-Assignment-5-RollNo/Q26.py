"""Python Programming Assignment 5 - Question 26."""

with open("append_read.txt", "a+") as f:
    f.write("Added text\n")
    f.seek(0)
    print(f.read())
