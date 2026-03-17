# FREEZE CODE BEGIN
def greet(name):
    return f"Hello, {name}!"

def flip(input_string):
    return input_string[::-1]

def count_letters(input_string, letter):
    count = 0
    for char in input_string:
        if char == letter:
            count += 1
    return count

if __name__ == "__main__":
  print("This file is being run directly.")
# FREEZE CODE END


def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

def exponent(base, exp):
    return base ** exp

def modulo(num1, num2):
    if num2 == 0:
        return "Error: Modulo by zero is not allowed."
    return num1 % num2

def floor_divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 // num2

def absolute(num):
    return abs(num)

#Parte 2
def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

#Parte 3
def exponent(base, exp):
    return base ** exp


def modulo(num1, num2):
    if num2 == 0:
        return "Error: Modulo by zero is not allowed."
    return num1 % num2

#Parte 4
def floor_divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    
    result = num1 // num2
    
    # asegurar tipo correcto
    if isinstance(num1, float) or isinstance(num2, float):
        return float(result)
    
    return result


def absolute(num):
    return abs(num)