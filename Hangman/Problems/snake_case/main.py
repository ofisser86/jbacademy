input_name = input()
to_snake_case = ''
for i in input_name:
    if i.isupper():
        to_snake_case += '_' + i.lower()
    else:
        to_snake_case += i
print(to_snake_case)
