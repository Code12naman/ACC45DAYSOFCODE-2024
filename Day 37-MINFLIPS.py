for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    summ=0
    i=0
    while(n>i):
        summ+=a[i]
        i+=1
    if(n%2==0):
        print(abs(summ)//2)
    else:
        print(-1)
