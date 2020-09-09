max_number = 0
res_string = ''
while True:
    string = input()
    if not any(map(str.isdigit, string)):
        break

    if int(string[string.index(' '):]) > max_number:
        max_number = int(string[string.index(' '):])
        res_string = string[:string.index(' ')]

print(res_string)
