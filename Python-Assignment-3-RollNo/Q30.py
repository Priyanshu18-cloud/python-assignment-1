"""Python Programming Assignment 3 - Question 30."""

numbers = [1, 2, 3, 4, 5, 6]
print("Even:", sum(n%2==0 for n in numbers))
print("Odd:", sum(n%2!=0 for n in numbers))
