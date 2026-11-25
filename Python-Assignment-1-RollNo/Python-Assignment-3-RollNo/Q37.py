"""Python Programming Assignment 3 - Question 37."""

items = [10, 40, 20, 30]
u = sorted(set(items))
print("Second largest:", u[-2] if len(u) >= 2 else "Not available")
