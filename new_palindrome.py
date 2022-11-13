n = int(input())
s = input().strip()
 
def divide(string):
    x = '@'
    for c in string:
        x += '#' + c
    x += '#&'
    left = 0
    right = 0
    ln = len(x)
    counter = [0] * ln
    for i in range(1, ln - 1):
        mirror = 2 * left - i
        if right > i:
            counter[i] = min(right - i, counter[mirror])
        while x[i + counter[i] + 1] == x[i - counter[i] - 1]:
            counter[i] += 1
        if i + counter[i] > right:
            left = i
            right = i + counter[i]
    longest = pos = 0
    for i in range(ln):
        if counter[i] > longest:
            pos = i
            longest = counter[i]
    return string[(pos - longest - 1) // 2:(pos + longest - 1) // 2]
 
depth = 0
prev = s[0]
while True:
    if len(s) == 1:
        break
    s = divide(s)
    if not len(s):
        s = prev
        break
    elif len(s) == 1 or len(s) % 2 == 1:
        break
    else:
        s = s[:len(s) // 2]
        prev = s[0]
        depth += 1
print(depth)
print(s)
