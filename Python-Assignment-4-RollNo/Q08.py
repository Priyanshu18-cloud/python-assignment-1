"""Python Programming Assignment 4 - Question 8."""

import math
a, b = 12, 18
g = math.gcd(a, b)
l = abs(a*b)//g
print("GCD:", g, "LCM:", l)
