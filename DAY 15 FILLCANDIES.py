# cook your dish here
def min_bags_needed(T, test_cases):
    results = []
    for i in range(T):
        N, K, M = test_cases[i]
        bag_capacity = K * M
        # Calculating the minimum number of bags using integer division
        bags_needed = (N + bag_capacity - 1) // bag_capacity
        results.append(bags_needed)
    return results

# Reading input
T = int(input())  # number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Getting the result
results = min_bags_needed(T, test_cases)

# Outputting the result
for result in results:
    print(result)
    