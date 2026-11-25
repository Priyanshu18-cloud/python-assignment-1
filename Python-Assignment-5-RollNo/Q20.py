"""Python Programming Assignment 5 - Question 20."""

with open("numbers.txt", "w") as f:
    for n in range(1, 101): f.write(f"{n}\n")
