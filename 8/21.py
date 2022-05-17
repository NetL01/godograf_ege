a = 'ЛЕТО'
mn = set()
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                m = a1+a2+a3+a4
                if a1 == 'Л' or a1 == 'Т':
                    mn.add(m)
print(len(mn))
                    
