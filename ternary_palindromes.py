for _ in range(int(input())):
    s = input()
    l = len(s)
    if l == 1:
        print(2)
    elif l == 2 and s[0]!=s[1]:
        print(2)
    else:
        a = [s.count("0"), s.count("1"), s.count("2")]
        if max(a) - min(a) > 1 or 0 in a:
            print(0)
        elif a[0] == a[1] and a[1] == a[2]:
            print(6)
        else:
            print(2)
