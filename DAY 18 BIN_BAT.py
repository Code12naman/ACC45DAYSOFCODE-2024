# cook your dish here
import math

def total_event_time(T, test_cases):
    results = []
    for N, A, B in test_cases:
        rounds = int(math.log2(N))  # Number of rounds is log2(N)
        breaks = rounds - 1  # Number of breaks is one less than the number of rounds
        total_time = (rounds * A) + (breaks * B)
        results.append(total_time)
    return results

# Reading input
T = int(input())  # number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Getting the result
results = total_event_time(T, test_cases)

# Outputting the result
for result in results:
    print(result)
    