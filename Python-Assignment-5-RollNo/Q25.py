"""Python Programming Assignment 5 - Question 25."""

with open("write_read.txt", "w+") as f:
    f.write("Hello file")
    f.seek(0)
    print(f.read())
