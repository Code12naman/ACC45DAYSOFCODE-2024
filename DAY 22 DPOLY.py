# cook your dish here
# Function to find the degree of the polynomial
def find_degree_of_polynomial(test_cases):
    for case in test_cases:
        N, coefficients = case
        # Traverse the coefficients from last to first
        for i in range(N-1, -1, -1):
            if coefficients[i] != 0:
                print(i)
                break

# Input reading and processing
T = int(input())  # Number of test cases
test_cases = []

for _ in range(T):
    N = int(input())  # Number of terms
    coefficients = list(map(int, input().split()))  # Coefficients of the polynomial
    test_cases.append((N, coefficients))

# Find and print the degree for each polynomial
find_degree_of_polynomial(test_cases)
