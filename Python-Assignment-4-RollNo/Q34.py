"""Python Programming Assignment 4 - Question 34."""

def count_case(s): return sum(c.isupper() for c in s), sum(c.islower() for c in s)
print(count_case("PyThOn"))
