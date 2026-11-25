"""Python Programming Assignment 3 - Question 19."""

s = input("Enter string: ")
for ch in dict.fromkeys(s): print(ch, ":", s.count(ch))
