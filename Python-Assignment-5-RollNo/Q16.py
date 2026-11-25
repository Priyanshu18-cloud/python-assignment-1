"""Python Programming Assignment 5 - Question 16."""

with open("write_demo.txt", "w") as f: f.write("Write mode replaces old content.")
with open("write_demo.txt", "a") as f: f.write("\nAppend mode adds content.")
