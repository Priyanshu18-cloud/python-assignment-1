"""Python Programming Assignment 3 - Question 3."""

s = input("Enter string: ")
v = sum(ch.lower() in "aeiou" for ch in s if ch.isalpha())
c = sum(ch.isalpha() and ch.lower() not in "aeiou" for ch in s)
print("Vowels:", v, "Consonants:", c)
