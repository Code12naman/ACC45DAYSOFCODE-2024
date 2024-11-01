# Number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read current score A:B
    A, B = map(int, input().split())
    # Read target score C:D
    C, D = map(int, input().split())
    
    # Check if the target score is achievable
    if C >= A and D >= B:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
