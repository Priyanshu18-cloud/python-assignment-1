"""Python Programming Assignment 2 - Question 36."""

n = int(input("Enter integer: "))
sign = -1 if n < 0 else 1
n = abs(n)
rev = 0
while n > 0: rev = rev*10 + n%10; n //= 10
print(sign * rev)
