"""Python Programming Assignment 2 - Question 39."""

n = int(input("Enter number: "))
prime = n > 1
for i in range(2, int(n**0.5)+1):
    if n % i == 0: prime = False; break
print("Prime" if prime else "Not prime")
