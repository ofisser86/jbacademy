chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

coins = int(input())
plural = ''

if chicken <= coins < goat:
    print(f"{coins // chicken} chicken{'' if coins // chicken == 1 else 's'}")
elif goat <= coins < pig:
    if coins // goat > 1:
        plural = 's'
    print(f"{coins // goat} goat{plural}")
elif pig <= coins < cow:
    if coins // pig > 1:
        plural = 's'
    print(f"{coins // pig} pig{plural}")
elif cow <= coins < sheep:
    if coins // cow > 1:
        plural = 's'
    print(f"{coins // cow} cow{plural}")
elif coins < chicken:
    print(None)
else:
    print(f"{coins // sheep} sheep")
