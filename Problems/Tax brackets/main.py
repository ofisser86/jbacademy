tax = 0
income = int(input())
if 15527 < income <= 42707:
    tax = 0.15
elif 42707 < income <= 132406:
    tax = 0.25
elif income >= 132407:
    tax = 0.28

calculated_tax = round(income * tax)
print(f"The tax for {income} is {int(tax*100)}%. That is {calculated_tax} dollars!")
