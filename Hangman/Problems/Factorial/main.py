N = int(input())
i = 1
fac = 1
if N != 0:
    while i <= N:
        fac *= i
        i += 1
print(fac)
