# cook your dish here
import sys

# Function to find minimum time to catch the thief
def catch_the_thief(test_cases):
    results = []
    for X, Y in test_cases:
        if X == Y:
            results.append(0)
        else:
            results.append(abs(X - Y))
    return results

# Input reading
T = int(input().strip())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Solving the problem
results = catch_the_thief(test_cases)

# Output results
sys.stdout.write("\n".join(map(str, results)) + "\n")
