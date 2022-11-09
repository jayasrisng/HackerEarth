'''
Problem
Xsquare loves to play with the coins very much. Today , he has N stacks of coins . Each stack of coins has some non zero height Hi equal to the number of coins on that stack ( considering all the coins are identical and each coin has a height of 1 unit ) .

In one move, Xsquare can select any number of consecutive stacks of coins such that the height of each selected stack of coins Hi ≤ K . Once such a sequence of stacks is chosen , Xsquare can collect any number of coins from the chosen sequence of stacks .

Xsquare wonders what is the maximum number of coins that he can collect this way ?

INPUT
First line of input contains a single integer T denoting the number of test cases . First line of each test case contains two space separated integers N and K where N being the number of stacks of coins. Second line of each test case contains N space separated integers denoting the number of coins Hi on each stack .

OUTPUT
For each test case , Print the maximum number of coins Xsquare can collect following the above gaming strategy.

Detailed Question : https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/xsquare-and-coin-collection-2/
'''

def coins(n,h,k):
    a=b=0
    for i in h:
        if(i<=k):
            a+=i
            b=max(a,b)
        else:
            a=0
    print(b)
 
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    coins(n,h,k)
