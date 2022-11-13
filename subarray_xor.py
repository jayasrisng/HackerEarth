from sys import stdin
from itertools import accumulate
 
def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    a = [0] +list(accumulate(a))
    m = 0
    maxsum = a[-1]
    for i in range(1,n):
        for j in range(i,n):
            x = a[i]^(maxsum-a[j])
            if x > m:
                m = x
    print(m)
 
if __name__=="__main__":main()
