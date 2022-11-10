'''
Problem
You are given an array  of  integers and  queries. In each query, you are given an integer .

Your task is to find the minimum index greater than  such that:

Sum of digits of  is greater than the sum of digits of 
 Ai < Aj 
If there is no answer, then print -1.

Input format

The first line contains two numbers  and .
The next line contains  numbers.
Next  lines contain  queries.
Output format

Print the answer as described in the problem

Detailed Question : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/yassers-conditions-6cc26a09/
'''

n,q = map(int, input().split())
lst = list(map(int, input().split()))

def digitSum(ds):
    d = 0
    for i in ds:
        d += int(i)
    return d
    
for i in range(q):
    t = int(input())
    ls = str(lst[t-1])
    d1 = digitSum(ls)
    res = 0
    for a in range(t-1, n):
        if(lst[a]>lst[t-1] and digitSum(str(lst[a]))<d1):
            print(a+1)
            res = 1
            break

    if(res==0):
        print(-1)
