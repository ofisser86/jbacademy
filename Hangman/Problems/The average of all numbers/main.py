# put your python code here

a = int(input())
b = int(input())
# summa = []
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         summa.append(i)
#
# print(sum(summa) / len(summa))

print(((a + 3 - a % 3 if a % 3 else a) + (b - b % 3 if b % 3 else b)) / 2)
