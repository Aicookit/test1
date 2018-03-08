from itertools import combinations
lottey=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i=combinations(lottey,5)
j=list(i)
for a in j:
    print(a)
b=len(j)
print('total:',b)