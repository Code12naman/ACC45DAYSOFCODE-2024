import math

def reach_fast(T, test_cases):
    results = []
    for case in test_cases:
        A, B, K = case
        distance = abs(A - B)
        steps = math.ceil(distance / K)
        results.append(steps)
    return results

# Input reading
T = int(input())  # number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get the result
results = reach_fast(T, test_cases)

# Output the result
for result in results:
    print(result)
