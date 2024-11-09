# cook your dish here
t = int(input())
for _ in range(t):
    Array_Size, Max_limit = map(int, input().split())
    Array_A = list(map(int, input().split()))
    Distance = 0
    for Num in Array_A:
        Distance += max(Max_limit - Num, Num - 1)
    print(Distance)