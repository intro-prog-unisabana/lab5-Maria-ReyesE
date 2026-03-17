

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

#FREEZE CODE BEGIN
a = int(input("Enter a number:\n"))
b = int(input("Enter a number:\n"))
c = int(input("Enter a number:\n"))

max_val = find_max(a, b, c)

print("Maximum value:", max_val)
#FREEZE CODE END
