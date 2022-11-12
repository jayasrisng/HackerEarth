from itertools import accumulate
import sys
 
def calc_func():
 
    total = 0
    k = 1
    for i in range(N):
        if i not in indexes:
            total += k*arr[i]
            k += 1 
 
    return total
    
for _ in range(int(sys.stdin.readline())):
 
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    sums = [0] + list(accumulate(arr))
 
    negs = [(x, i) for i, x in enumerate(arr) if x < 0]
 
    if len(negs) == 0:
        print(sum((i+1)*x for i, x in enumerate(arr)))
        continue
 
    if len(negs) == N:
        print(0)
        continue
    
    indexes = set()
    total_deleted = 0
    max_value = calc_func()
 
    while True:
 
        max_index = -1
        deleted = 0
        prev_deleted = 0
        curr_max = max_value
 
        for i in range(len(negs)):
 
            if negs[i][1] in indexes:
                prev_deleted += negs[i][0]
                deleted += 1
                continue
 
            next_deleted = total_deleted - prev_deleted
            value = curr_max - (negs[i][1] - deleted + 1)*negs[i][0] - (sums[-1]- sums[negs[i][1]+1] - next_deleted)
            
            #print(curr_max, value, negs[i])
            if value > max_value:
                max_index = negs[i][1]
                max_value = value
 
        if max_index == -1:
            break
 
        total_deleted += arr[max_index]
        indexes.add(max_index)
        #print(indexes)
 
    total = calc_func()
    print(total)
