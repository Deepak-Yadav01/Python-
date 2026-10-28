number = 10
original_number = number
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1 
print(f"Factorial of {original_number} is: {factorial}")   