max_dels = 0
max_del = 0
for i in range(286564, 287270):
    for g in range(1, i+1):
        dels = []
        if i % g == 0:
            dels.append(g)
            if max_dels < len(dels):
                max_dels = len(dels)
                max_del = i
print(max_del)

dels = []
count = 0
for i in range(1, 286564+1):
    if 286564 % i == 0:
        dels.append(i)
        count += 1
print(count, dels[-1], dels[-2])
               
