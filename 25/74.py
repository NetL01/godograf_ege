count = 0
for i in range(2, 30000+1):
    dels = []
    for g in range(1, i+1):
        if i % g == 0:
            dels.append(g)
    if i < sum(dels):
        count += 1
print(count)
        
