amount_of_atoms = int(input())
final_quantity_of_atoms = int(input())

count = 0
while amount_of_atoms >= final_quantity_of_atoms:
    amount_of_atoms = amount_of_atoms / 2
    count += 1

print(count * 12)
