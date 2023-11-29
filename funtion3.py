def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

result = divide_numbers(10, 2)
print(result)
