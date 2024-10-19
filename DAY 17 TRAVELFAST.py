# cook your dish here
def faster_transport(T, test_cases):
    results = []
    for X, Y in test_cases:
        if X < Y:
            results.append("BIKE")
        elif X > Y:
            results.append("CAR")
        else:
            results.append("SAME")
    return results

# Reading input
T = int(input())  # number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Getting the result
results = faster_transport(T, test_cases)

# Outputting the result
for result in results:
    print(result)
    