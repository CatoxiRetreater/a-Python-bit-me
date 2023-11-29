with open('input.txt', 'r') as file:
    data = file.read()
    print(data)

with open('output.txt', 'w') as file:
    file.write('Hello, World!')
