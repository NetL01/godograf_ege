max_sum_dels = 0
max_num = 0
for i in range(268220, 270335+1):
    dels = []
    for g in range(1, i+1):
        if i % g == 0:
            dels.append(g)
    if len(dels) <= 4:
        if max_sum_dels < sum(dels):
            max_sum_dels = sum(dels)
            max_num = i
# print(max_num) --> 270302
dels = []
for i in range(1, 270302+1):
    if 270302 % i == 0:
        dels.append(i)
dels.sort()
print(max_sum_dels, len(dels), *dels) 
        
