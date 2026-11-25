"""Python Programming Assignment 5 - Question 14."""

text = input("Enter text: ")
with open("user.txt", "w") as f: f.write(text)
