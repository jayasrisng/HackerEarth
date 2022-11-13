from sys import stdin
 
def Adda(x,qu):
    global n, AIBA
    i = x
    while(i<=n):
        AIBA[i] = AIBA[i] + qu
        i = i + ((i^(i-1))&i)
    return 0
 
def Computea(x):
    global AIBA
    ret = 0
    i = x
    while(i>0):
        ret = ret + AIBA[i]
        i = i - ((i^(i-1))&i)
    return ret
 
def Addb(x,qu):
    global n, AIBB
    i = x
    while(i<=n):
        AIBB[i] = AIBB[i] + qu
        i = i + ((i^(i-1))&i)
    return 0
 
def Computeb(x):
    global AIBB
    ret = 0
    i = x
    while(i>0):
        ret = ret + AIBB[i]
        i = i - ((i^(i-1))&i)
    return ret
 
def Addc(x,qu):
    global n, AIBC
    i = x
    while(i<=n):
        AIBC[i] = AIBC[i] + qu
        i = i + ((i^(i-1))&i)
    return 0
 
def Computec(x):
    global AIBC
    ret = 0
    i = x
    while i:
        ret = ret + AIBC[i]
        i = i - ((i ^ (i - 1)) & i)
    return ret
 
def main ():
    global n, AIBA, AIBB, AIBC
    AIBA = [0]*100003
    AIBB = [0]*100003
    AIBC = [0]*100003
    t = int(input())
    for ia in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        for h in range(n):
            j = h+1
            x = Adda(j,j*a[h])
            x = Addb(j,a[h])
            x = Addc(j,j*j*a[h])
        q = int(input())
        for j in range(q):
            tip,l,r = map(int,input().split())
            if(tip==1):
                x = Adda(l,l*(r-a[l-1]))
                x = Addb(l,r-a[l-1])
                x = Addc(l,l*l*(r-a[l-1]))
                a[l-1] = r
            else:
                sa = Computea(r)-Computea(l-1)
                sb = Computeb(r)-Computeb(l-1)
                sc = Computec(r)-Computec(l-1)
                rez = sa*(l+r)-sb*(l-1)*(r+1)-sc
                print(rez)
        for j in range(n):
            AIBA[j+1] = 0
            AIBB[j+1] = 0
            AIBC[j+1] = 0
 
if __name__ == "__main__": main ()
