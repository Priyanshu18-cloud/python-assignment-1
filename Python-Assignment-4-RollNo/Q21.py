"""Python Programming Assignment 4 - Question 21."""

def digit_sum(n): return sum(int(d) for d in str(abs(n)))
print(digit_sum(1234))
