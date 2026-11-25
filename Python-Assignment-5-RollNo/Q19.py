"""Python Programming Assignment 5 - Question 19."""

n = int(input("Table number: "))
with open("table.txt", "w") as f:
    for i in range(1, 11): f.write(f"{n} x {i} = {n*i}\n")
