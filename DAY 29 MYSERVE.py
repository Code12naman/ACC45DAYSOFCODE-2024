# cook your dish here
# Number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Input the scores for Alice and Bob
    P, Q = map(int, input().split())
    
    # Calculate total points
    total_points = P + Q
    
    # Determine whose serve it is
    if (total_points // 2) % 2 == 0:
        print("Alice")
    else:
        print("Bob")
        