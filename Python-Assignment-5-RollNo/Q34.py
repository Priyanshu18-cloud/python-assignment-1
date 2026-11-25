"""Python Programming Assignment 5 - Question 34."""

word = input("Word: ")
with open("sample.txt", "r") as f: print("Occurrences:", f.read().split().count(word))
