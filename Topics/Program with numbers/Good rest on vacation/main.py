def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        print(x)
    else:
        y = x + (5 - remainder)
        print(y)

closest_higher_mod_5(43)
