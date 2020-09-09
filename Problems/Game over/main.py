scores = input().split()
# put your python code here
count = 0
new_list = []
for i in scores:
    if count == 3:
        print("Game over")
        print(new_list.count("C"))
        break
    if i == 'I':
        count += 1

    new_list.append(i)
else:
    print("You won")
    print(new_list.count("C"))
