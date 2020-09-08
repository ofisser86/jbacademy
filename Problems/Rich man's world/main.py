n = int(input())
count = 0
while n < 700000:
    n += n * 0.071
    count += 1
print(count)
