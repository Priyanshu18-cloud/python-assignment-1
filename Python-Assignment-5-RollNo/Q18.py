"""Python Programming Assignment 5 - Question 18."""

name, roll, marks = "Aman", 101, 88
with open("student.txt", "w") as f: f.write(f"Name: {name}\nRoll: {roll}\nMarks: {marks}")
