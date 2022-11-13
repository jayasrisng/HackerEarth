from sys import stdin
from heapq import heappush, heappop
 
def main ():
    read = stdin.readline
    t = int (read ())
    for t_ in range (t):
        x, y, z = map (int, read ().split ())
        k = int (read ())
        bx = sorted (map (int, read ().split ()), reverse = True)
        by = sorted (map (int, read ().split ()), reverse = True)
        bz = sorted (map (int, read ().split ()), reverse = True)
        ix = 0; iy = 0; iz = 0
        h = [(-bx [ix] - by [iy] - bz [iz], (ix, iy, iz))]
        seen = set ()
        sm = 0
        while k:
            v, (ix, iy, iz) = heappop (h)
            sm -= v
            ixn = ix + 1; iyn = iy + 1; izn = iz + 1
            if ixn < x and (ixn, iy, iz) not in seen:
                heappush (h, (-bx [ixn] - by [iy] - bz [iz], (ixn, iy, iz)))
                seen.add ((ixn, iy, iz))
            if iyn < y and (ix, iyn, iz) not in seen:
                heappush (h, (-bx [ix] - by [iyn] - bz [iz], (ix, iyn, iz)))
                seen.add ((ix, iyn, iz))
            if izn < z and (ix, iy, izn) not in seen:
                heappush (h, (-bx [ix] - by [iy] - bz [izn], (ix, iy, izn)))
                seen.add ((ix, iy, izn))
            k -= 1
        print (sm)
 
if __name__ == "__main__": main ()
