"""Python Programming Assignment 5 - Question 42."""

import os
path = "sample.txt"
if os.path.exists(path): print("Name:", os.path.basename(path), "Size:", os.path.getsize(path), "Bytes")
else: print("File does not exist")
