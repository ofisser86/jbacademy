# put your python code here
summa = []
while True:
    n = int(input())
    summa.append(n)
    if sum(summa) == 0:
        break
print(sum(i * i for i in summa))
