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