import math
 
def convertTime(time):
    a,b,c = time.split(':')
 
    second = 0
    second+= int(a)*3600 + int(b)*60 +int(c)
    return second 
 
def Attendance(arr,classTime):
    # print(classTime)
    arr.sort(key= lambda x:(x[0]))
    # print(arr)
    
    if arr[0][0]> classTime[0] or arr[-1][0]<classTime[1]:
        print('aaaa')
        return [0]
 
 
    minStd= 1000000
    counter=0
 
    i=0
 
    c=0
    while i<len(arr):
        time,ad,idx = arr[i]
 
        if ad=='a':
            c+=1
        else:
            c-=1
        i+=1
 
        while i<len(arr) and arr[i][0]==arr[i-1][0]:
            if arr[i][1]=='a':
                c+=1
            else:
                c-=1
            i+=1
 
        if c<minStd and i<len(arr):
            minStd= c 
            counter= 1
        elif c==minStd:
            counter+=1
    
    if minStd==0:
    
        return [0] 

    student=set()
    p=0
    q=0
 
    c=0 
    i=0
 
    while i<len(arr):
 
        time,ad,idx = arr[i] 
 
        if ad=='a':
            c+=1
            student.add(idx)
        else:
            c-=1
            student.remove(idx)
        i+=1
        
 
        while i<len(arr) and arr[i][0]==arr[i-1][0]:
            if arr[i][1]=='a':
                c+=1
                student.add(arr[i][2])
            else:
                c-=1
                student.remove(arr[i][2])
            i+=1
        
        if c== minStd:
            if i==len(arr):
                continue
            elif i==0:
                dt = arr[i][0]- classTime[0]
            else:
                dt = arr[i][0]- arr[i-1][0]
            
            q+=dt 
 
            if 0 in student:
                p+= dt
    
    return [p,q]
 
n = int(input()) 
classTime = list(input().split()) 
classTime[0]= convertTime(classTime[0]) 
classTime[1]= convertTime(classTime[1])
arr=[]
 
for _ in range(n):
    x = list(input().split())
    idx = int(x[0]) -1
 
    for i in range(2,len(x)):
        t= convertTime(x[i])
        if i&1:
            arr.append((t,'d',idx))
        else:
            arr.append((t,'a',idx)) 
 
p= Attendance(arr,classTime)
 
if len(p)==0 or p[0]==0:
    print(0)
else:
    d = math.gcd(p[0],p[1])
    p[0]= p[0]//d
    p[1]= p[1]//d
    print('{}/{}'.format(p[0],p[1]))
