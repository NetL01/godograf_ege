a = 'ТОК'
count = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    for a6 in a:
                        m = a1+a2+a3+a4+a5+a6
                        if a1 == 'Т' or a1 == 'К':
                            count += 1
print(count)
