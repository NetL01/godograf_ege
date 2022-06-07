for i in range(100812, 100924):
    a = i**0.5
    if a % 1 != 0:
        dels = []
        for g in range(1, i+1):
            if i % g == 0:
                dels.append(g)
        if len(dels) == 6:
            print(dels)
