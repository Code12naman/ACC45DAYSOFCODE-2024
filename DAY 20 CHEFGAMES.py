# cook your dish here
def chefland_games(T, test_cases):
    results = []
    for case in test_cases:
        if sum(case) == 0:  # If the sum of the decisions is 0, all referees said "inside"
            results.append("IN")
        else:
            results.append("OUT")
    return results

# Reading input
T = int(input())  # number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Getting the result
results = chefland_games(T, test_cases)

# Outputting the result
for result in results:
    print(result)
