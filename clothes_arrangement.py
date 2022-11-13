from sys import stdin, stdout
from collections import defaultdict
from bisect import insort, bisect_right
 
class Fenwick_Tree:
    def __init__(self, n, arr=[]):
        self.tree = [0]*(n+1)
        self.n = n
        
        if arr:
            self.initialize(arr)
        
    def getSum(self, idx):
        sm = 0
        idx += 1      
        while idx > 0:
            sm += self.tree[idx] 
            idx -= idx & (-idx)
        
        return sm
 
    def updateBIT(self, ind, val):
        ind += 1;      
        while (ind <= self.n):
            self.tree[ind] += val; 
            ind += ind & (-ind); 
  
    def sum_arr(self, x, BITTree2):
        return (self.getSum(x) * x) - BITTree2.getSum(x)
  
    def updateRange(self, BITTree2, val, l, r):      
        self.updateBIT(l, val)
        self.updateBIT(r+1, -val)      
        BITTree2.updateBIT(l, val*(l-1))
        BITTree2.updateBIT(r+1, -val*r)
        
def zero_count(arr, x):
    return len(arr) - bisect_right(arr, x)
    
def solve():
    N = int(stdin.readline())    
    A = [int(k) for k in stdin.readline().split()]    
    indexes = defaultdict(list)    
    results = []
    
    for i in range(N):
        indexes[A[i]].append(i)
    
    MAX = N*2
    BIT1 = Fenwick_Tree(MAX)
    BIT2 = Fenwick_Tree(MAX)
    
    for _ in range(int(stdin.readline())):
        q = stdin.readline().split()
        
        if q[0] == "1":
            C = int(q[1])
            A.append(C)
            indexes[C].append(N)
            N += 1
        else:
            C = int(q[1])
            K = int(q[2])
            if K > len(indexes[C]):
                results.append(-1)
            else:
                i = indexes[C][len(indexes[C])-K]
                zeros = BIT1.getSum(MAX-1) - BIT1.getSum(i-1)
 
                A[i] = 0
                
                BIT1.updateRange(BIT2,1,i,MAX-1) 
                del indexes[C][len(indexes[C])-K]
                results.append(N - i - 1 - zeros)
                
    stdout.write ('\n'.join(str(k) for k in results))
                
solve()
