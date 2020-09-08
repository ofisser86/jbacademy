n = int(input())
res = []
for _ in range(n):
    m = int(input())
    if m % 7 == 0:
        res.append(m * m)

for i in res:
    print(i)
