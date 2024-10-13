# cook your dish here
def count_notebooks(T, test_cases):
    results = []
    for N in test_cases:
        # Each kg of pulp can produce 10 notebooks
        results.append(10 * N)
    return results

# Reading input
T = int(input())  # number of test cases
test_cases = [int(input()) for _ in range(T)]

# Getting the result
results = count_notebooks(T, test_cases)

# Outputting the result
for result in results:
    print(result)
    