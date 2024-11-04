# cook your dish here
# Reading the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N = int(input())  # Number of bits for this test case
    if N % 4 == 0:
        print("Good")
    else:
        print("Not Good")
