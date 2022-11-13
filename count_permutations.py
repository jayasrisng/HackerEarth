MOD = 10 ** 9 + 7
for _ in range(int(input())):
    N = int(input())
    ways = 1
    m = 0
    for i, num in enumerate(map(int, input().split(" "))):
        if num < m or num <= i:
            print(0)
            break
        elif num == m:
            ways = ways * (m - i) % MOD
        else:
            m = num
    else:
        print(ways)
