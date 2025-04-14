def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply(1, 2, 3))  # Output: 6
print(multiply(4, 5))     # Output: 20
print(multiply(2, 3, 4, 5))  # Output: 120