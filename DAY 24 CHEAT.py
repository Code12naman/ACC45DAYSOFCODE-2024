# cook your dish here
# Function to calculate the number of Tuesdays
def count_tuesdays(N):
    if N < 2:
        return 0
    # Count how many Tuesdays fall within the first N days
    return (N - 2) // 7 + 1

# Input reading and processing
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())  # Number of spooky days
    print(count_tuesdays(N))
    