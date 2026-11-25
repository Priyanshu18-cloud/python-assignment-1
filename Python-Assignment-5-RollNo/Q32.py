"""Python Programming Assignment 5 - Question 32."""

with open("sample.txt", "r") as f: text = f.read()
print("Uppercase:", sum(c.isupper() for c in text))
print("Lowercase:", sum(c.islower() for c in text))
