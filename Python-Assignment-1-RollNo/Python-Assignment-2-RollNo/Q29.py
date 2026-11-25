"""Python Programming Assignment 2 - Question 29."""

n = int(input("Enter number: "))
print("Divisible by both" if n % 5 == 0 and n % 11 == 0 else "Not divisible by both")
