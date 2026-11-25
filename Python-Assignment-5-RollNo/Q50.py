"""Python Programming Assignment 5 - Question 50."""

import os
path = "temporary.txt"
with open(path, "w") as f: f.write("Python file handling example.")
with open(path, "r") as f: print(f.read())
os.remove(path)
print("File closed and deleted.")
