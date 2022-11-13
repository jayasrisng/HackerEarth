import sys 
def rl():
    return sys.stdin.readline()
 
ind1 = -1
C = []
count = 0
def findInd1(A,N):
    global ind1
    global C
    ind1 = A.index(1)
    C = [0]*N
    c= 1
    for i in range(ind1,N):
        C[i] = c
        c+=1
    for i in range(0,ind1):
        C[i] = c
        c+=1
 
def computeQuery(A,B,X,N,Q):
    global ind1
    global C
    global count
    if Q == 0:
        A[X] = B
        count = ind1
        for i in range(N):
            if(A[i] != C[i]):
                count +=1
 
        sys.stdout.write(str(count)+"\n")
    else:
        if(A[X] == C[X] and B!=C[X]):
            count +=1
        elif(A[X] != C[X] and C[X] == B):
            count -=1
        A[X] = B
        sys.stdout.write(str(count)+"\n")
 
def main():
    N = int(rl())
    A = list(map(int,rl().split()))
    findInd1(A,N)
    Q =int(rl())
    for q in range(Q):
        X,B = map(int,rl().split())
        computeQuery(A,B,X-1,N,q)
 
 
main()
