from sys import stdin
 
def main ():
    read = stdin.readline
    mod = 1000000007
    n = int (read ())
    a = list (map (int, read ().split ()))
    b = list (map (int, read ().split ()))
    sumab = sum (k * l for k, l in zip (a, b)) % mod
    print (((sum (i * i for i in a) % mod) * (sum (j * j for j in b) % mod) - sumab * sumab % mod) % mod)
 
if __name__ == "__main__": main ()
