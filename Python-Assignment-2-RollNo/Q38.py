"""Python Programming Assignment 2 - Question 38."""

n = abs(int(input("Enter number: ")))
total = 0
while n > 0: total += n%10; n //= 10
print("Sum of digits =", total)
