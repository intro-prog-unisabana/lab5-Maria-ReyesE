import os
import math

# Directorio actual
print("Current working directory:", os.getcwd())

# Input
num = int(input("Enter an integer: "))

# Log base 2
log_val = math.log2(num)
print(f"Log base 2 of {num} is: {log_val}")

# Floor y Ceiling
print("Floor:", math.floor(log_val))
print("Ceiling:", math.ceil(log_val))
