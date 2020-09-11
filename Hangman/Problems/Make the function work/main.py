def closest_higher_mod_5(x):
    if x % 5 == 0:
        return x
    return (5 - x % 10) + x if x % 10 < 5 else round(x, -1)
