total = 0
count = 0
while True:
    element = input()
    if element == '.':
        break
    total += int(element)
    count += 1

print(total / count)
