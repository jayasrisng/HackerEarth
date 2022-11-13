from math import floor
from fractions import Fraction

def rank(a, b, n):
    "Return the rank of the fraction x=a/b in F_n."
    A = [a * q // b for q in range(0, n+1)]
    for q in range(1, n+1):
        for i in range(q + q, n + 1, q):
            A[i] -= A[q]
    return sum(A)

def next_term(f1, f2, n):
    "Return next term in Farey Sequence F_n"
    t = (n + f1.denominator) // f2.denominator
    p = t * f2.numerator - f1.numerator
    q = t * f2.denominator - f1.denominator
    return Fraction(p, q)
 
 
def solve(n, k):
    
    if k == 1:
        return (0, 1)
   
    cutoff = n // 2
    if n % 2:
        cutoff += 1
    cutoff_posn = 2 + n - cutoff
    if k <= cutoff_posn:
        return (1, n - k + 2)
 
    low, high = 0, n
    X = 0
    R = 0
    while low < high:
        mid = (low + high) // 2
        r0 = rank(mid, n, n)
        if r0 == k - 1:
            X = mid
            R = r0
            break
        if r0 > k - 1:
            high = mid - 1
        else:
            X = mid
            R = r0
            low = mid + 1
 

    x0 = Fraction(X, n)
    if R == k - 1:
        return (x0.numerator, x0.denominator)
 
    j = X
    x1 = Fraction(1, 1)
    for q in range(1, n+1):
        p = ((j+1) * q - 1) // n
        g = Fraction(p, q)
        if g > x0:
            x1 = min(x1, g)
    if R == k:
        return (x1.numerator, x1.denominator)
    for _ in range(R + 2, k):
        x0, x1 = x1, next_term(x0, x1, n)
    return (x1.numerator, x1.denominator)
 
import sys 
def main():
    n, k = (int(i) for i in sys.stdin.readline().split())
    soln = solve(n, k)
    print("{}/{}".format(*soln)) 
 
if __name__ == '__main__':
    main()
