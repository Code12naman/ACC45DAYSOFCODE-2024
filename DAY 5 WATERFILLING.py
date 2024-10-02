# cook your dish here
T = int(input())

for _ in range(T):
    B1, B2, B3 = map(int, input().split())
    
    empty_count = B1 + B2 + B3
    
    if empty_count <= 1:
        print("Water filling time")
    else:
        print("Not now")
