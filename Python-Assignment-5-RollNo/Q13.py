"""Python Programming Assignment 5 - Question 13."""

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("lines.txt", "w") as f: f.writelines(lines)
