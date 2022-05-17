a = 'КОТ'
count = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    m = a1+a2+a3+a4+a5
                    if m.count('О') == 2:
                        count += 1
print(count)
                        
