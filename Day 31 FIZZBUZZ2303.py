# cook your dish here
# Number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the number of players Chef is considering
    N = int(input())
    
    # Calculate the number of ways to choose a captain and vice-captain
    result = N * (N - 1)
    
    # Output the result
    print(result)
    