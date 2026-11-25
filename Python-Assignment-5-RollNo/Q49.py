"""Python Programming Assignment 5 - Question 49."""

import os
os.rename("old.txt", "renamed.txt")
with open("renamed.txt", "r") as f: print(f.read())
