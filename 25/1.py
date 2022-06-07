for i in range(126849, 126872):
    a = i**0.5
    if a % 1 != 0:
        dels = []
        for g in range(1, i+1):
            if i % g == 0:
                dels.append(g)
        if len(dels) == 4:
            print(dels)
