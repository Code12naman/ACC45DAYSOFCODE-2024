# cook your dish here
# Read number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read the tastiness values for the ingredients
    a, b, c, d = map(int, input().split())
    
    # Calculate the possible sums of tastiness
    sum1 = a + c
    sum2 = a + d
    sum3 = b + c
    sum4 = b + d
    
    # Output the maximum possible sum
    print(max(sum1, sum2, sum3, sum4))
    