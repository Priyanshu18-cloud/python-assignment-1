"""Python Programming Assignment 5 - Question 48."""

import os
path = "sample.txt"
print("Exists:", os.path.exists(path))
if os.path.exists(path): print("Size:", os.path.getsize(path), "bytes")
