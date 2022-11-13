from sys import stdin
 
def main ():
    read = stdin.readline
    t = int (read ())
    bx, by, bz = map (int, read ().split ())
    bvx, bvy, bvz = map (int, read ().split ())
    mx, my, mz = map (int, read ().split ())
    mvx, mvy, mvz = map (int, read ().split ())
    def dist (x):
        bxx, byx, bzx = (bx + bvx * x, by + bvy * x, bz + bvz * x)
        mxx, myx, mzx = (mx + mvx * x, my + mvy * x, mz + mvz * x)
        dx = mxx - bxx; dy = myx - byx; dz = mzx - bzx;
        return (dx * dx + dy * dy + dz * dz)
    eps = 1e-7; 
    l = 0; r = t
    while (r - l > eps):
        m1 = l + (r - l) / 3;
        m2 = r - (r - l) / 3;
        f1 = dist (m1);
        f2 = dist (m2); 
        if (f1 > f2): l = m1;
        else: r = m2;
    print (dist (l) ** .5); 
 
if __name__ == "__main__": main ()
