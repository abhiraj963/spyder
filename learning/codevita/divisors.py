from functools import reduce
try:
    flag = 1
    while flag:
        T = int(input())
        if T > 0 or T < 16:
            flag = 0
    N = []
    for i in range(0,T):
        flag1 = 1
        while flag1:
            x = int(input())
            N.append(x)
            if N[i] > 0 or N[i] < ((10**15)+1):
                flag1 = 0
                
        
except:
    print('enter a number')


def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

for i in N:
    lst = list(factors(i))
    lst = [str(x) for x in lst]
    lst = sorted(lst)
    print(' '.join(lst))


