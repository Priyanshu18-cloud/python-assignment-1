"""Python Programming Assignment 5 - Question 12."""

names = ["Aman", "Riya", "Neha", "Raj", "Simran"]
with open("students.txt", "w") as f:
    for name in names: f.write(name + "\n")
