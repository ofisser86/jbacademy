# put your python code here
groups = [int(input()) for i in range(0, 3)]

desks = 0

for students_in_group in groups:
    if students_in_group % 2 == 0:
        desks += students_in_group / 2
    else:
        desks += (students_in_group + 1) / 2


print(int(desks))


