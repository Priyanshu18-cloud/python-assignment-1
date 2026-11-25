"""Python Programming Assignment 5 - Question 44."""

import os
path = "unwanted.txt"
if os.path.exists(path): os.remove(path); print("Deleted")
else: print("File not found")
