"""Python Programming Assignment 1 - Question 46."""

marks = []
for i in range(5):
    marks.append(float(input(f"Enter subject {i+1} marks: ")))
print("Total =", sum(marks))
