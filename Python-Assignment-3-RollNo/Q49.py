"""Python Programming Assignment 3 - Question 49."""

t = (1, 2, 3)
try: t[0] = 9
except TypeError: print("Tuple cannot be changed")
t = t + (4,)
print(t)
