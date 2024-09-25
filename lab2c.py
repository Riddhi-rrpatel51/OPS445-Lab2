#!/usr/bin/env python3
import sys

# Check if there are enough command line arguments
if len(sys.argv) < 3:
    print("Error: Missing arguments")
    sys.exit(1)

# Assign the first and second arguments to variables
name = sys.argv[1]
age = int(sys.argv[2])

# Print the output
print(f"Hi {name}, you are {age} years old.")

