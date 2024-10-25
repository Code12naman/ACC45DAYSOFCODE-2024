# cook your dish here
# Function to count the occurrences of START38 and LTIME108 in each test case
def count_contests(test_cases):
    for case in test_cases:
        N, contests = case
        start38_count = contests.count("START38")
        ltime108_count = contests.count("LTIME108")
        print(start38_count, ltime108_count)

# Input reading and processing
T = int(input())  # Number of test cases
test_cases = []

for _ in range(T):
    N = int(input())  # Number of problems
    contests = input().split()  # Contest codes (START38 or LTIME108)
    test_cases.append((N, contests))

# Count and print the number of problems for each contest
count_contests(test_cases)
