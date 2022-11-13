def solve(s1,s2,N):
    if s1 == s2:
        return "YES"
    flag = False
    s1_list = [0]*27
    s2_list = [0]*27
    for i in range(N):
        s1_list[ord(s1[i])-96] += 1
        s2_list[ord(s2[i])-96] += 1
    for i in range(1, 27):
        if s1_list[i] != s2_list[i]:
            return "NO"
        elif (s1_list[i] == s2_list[i] == 1) or (s1_list[i] == s2_list[i] == 0):
            pass
        else:
            flag = True
    if not flag:
        cnt = 0
        while(s1 != ''):
            ind = s2.find(s1[0])
            s1 = s1[1:]
            s2 = s2[:ind] + s2[ind+1:]
            cnt += ind
        return "YES" if cnt%2 == 0 else "NO"
    return "YES"
 
for _ in range(int(input())):
    N = int(input())
    s1 = input()
    s2 = input()
    print(solve(s1,s2,N))
