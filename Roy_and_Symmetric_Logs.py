'''
Problem:

Roy likes Symmetric Logos. How to check whether a logo is symmetric? Align the center of logo with the origin of Cartesian plane. Now if the colored pixels of the logo are symmetric about both X-axis and Y-axis, then the logo is symmetric. You are given a binary matrix of size N x N which represents the pixels of a logo.
1 indicates that the pixel is colored and 0 indicates no color.

Input:
First line contains T - number of test cases.
T test cases follow.
First line of each test case contains the N - size of matrix.
Next N lines contains binary strings of length N.

Output:
Print YES or NO in a new line for each test case

Detailed Question:
https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/roy-and-symmetric-logos-1/
'''

def x_axis(m):
    c=0
    for i in range(len(l)):
        if(l[i]==l[-(i+1)]):
            c+=1
    if(c==len(l)):
        return True
    else:
        return False
 
def y_axis(m):
    c=0
    for i in l:
        if(i==i[-1::-1]):
            c+=1
    if(c==len(l)):
        return True
    else:
        return False
  
t=int(input())
for i in range(t):
    l=[]
    n=int(input())
    for i in range(n):
        a=input()
        l.append(a)
    count=0
    for m in l:
        if(x_axis(m) and y_axis(m)):
            count+=1
    if(count==len(l)):
        print("YES")
    else:
        print("NO")
