import sys
sys.setrecursionlimit(10**6)
 
primes = [2,3,5,7,11,13,17,19,23,29,31,37]
 
def mov(t, pos, p, king,for0):
    if pos >= l or pos < 0 or pos in king:
        return False
    if pos == t:
        if p == 0 and pos == 0 and 0 not in king:
            for j in primes:
                if arr[pos] % j == 0:
                    op = mov(t, pos + j, p + 1, king, for0)
                    op2 = mov(t, pos - j, p + 1, king, for0)
 
                    if op:
                        return op 
                    if op2:
                        return op2
            return False
        if for0 != 0:
            u = (m-1) % (for0 + p)
            if u % 2 != 0:
                return True
            return False
        for j in range(t):
            if mov(j, t, 0, [], p):
                return True
 
    else:
        for j in primes:
 
            if arr[pos] % j == 0:
                king.append(pos)
                op = mov(t, pos+j, p + 1, king,for0)
                op2 = mov(t, pos - j, p + 1, king, for0)
                #print(t,"op",op,"pos+j",pos-j,"=====","op2",op2,"pos-j",pos-j)
                if op:
                    return op
 
                if op2:
                    return op2
 
        return False
 
for _ in range(int(input())):
    l = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    flag = False
    for i in range(l-1):
        if arr[i] % (l-i-1) == 0 and (l-i-1) in primes:
            if m == 1 and i == 0:
                flag =True
                break
            if mov(i, 0, 0,[],0):
                flag = True
                break
    if flag:
        print("YES")
    else:
        print("NO")
