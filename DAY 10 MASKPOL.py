t=int(input())
for i in range(t):
    n,a=map(int,input().split())
    if n>a:
        print(min(n-a,a))
        