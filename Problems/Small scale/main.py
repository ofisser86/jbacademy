numbers = []
while True:
    element = input()
    if element == '.':
        break
    numbers.append(float(element))
print(min(numbers))
