import time
import math
 
prime = []
pmult = []
noprime = {}
master = []
size = []
 
def fill_1_prime(limit):
    sqlimit = int(math.sqrt(limit))
    j = 0
    for i in range(2, limit+1):
        if (noprime.get(i) == None):
            #if (i <= sqlimit):
            prime.append([i])
            j += 1
            nxt = i
            while(nxt+i <= limit):
                noprime[nxt+i] = nxt+i
                nxt += i
    size.append(j)
 
mlimit = int(input()) 
num = int(input())
 
numl = [int(v) for v in input().split()]
fill_1_prime(mlimit)
dsum = 0
for i in prime:
    if (i[0]*i[0] <= mlimit):
        dsum += 1
        master.append([i[0],i[0]])
        pmult.append(i[0]*i[0])
    else:
        break
size.append(size[0]+dsum)
 
for i in range(0, num):
    arsize = numl[i]
    if (arsize <= len(size)):
        print(size[arsize -1], end=' ')
        continue
    start = len(size)+1
    for sz in range(start, arsize+1):
        if (len(master) == 0):
            break
        if (sz % 2 == 0):
            newl = []
            mid = len(master[0])//2
            tmult = []
            for i in range(0, len(master)):
                mul = pmult[i] * master[i][mid]
                if (mul <= mlimit):
                    newl.append(master[i])
                    newl[-1][mid+1:mid+1] = [master[i][mid]]
                    tmult.append(mul)
            master = newl
            pmult = tmult
        else:
            newl = []
            mid = len(master[0])//2
            tmult = []
            for i in range(0, len(master)):
                for pelem in prime:
                    mul = pmult[i] * pelem[0]
                    if (mul <= mlimit):
                        newl.append(master[i])
                        newl[-1] = newl[-1][0:mid] + pelem + newl[-1][mid:]
                        tmult.append(mul)
                    else:
                        break
            pmult = tmult
            master = newl
        size.append(size[-1] + len(master))

    print(size[-1], end=' ')
