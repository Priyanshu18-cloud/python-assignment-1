"""Python Programming Assignment 4 - Question 38."""

value = "global"
def show():
    value = "local"
    print(value)
show()
print(value)
