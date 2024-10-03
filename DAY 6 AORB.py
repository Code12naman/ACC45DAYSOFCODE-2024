# cook your dish here
def max_score(T, test_cases):
    results = []
    for X, Y in test_cases:
        # Score if A is solved first, then B
        score_A_first = (500 - X * 2) + (1000 - (X + Y) * 4)
        
        # Score if B is solved first, then A
        score_B_first = (1000 - Y * 4) + (500 - (X + Y) * 2)
        
        # Take the maximum of the two scores
        max_score = max(score_A_first, score_B_first)
        
        # Store the result
        results.append(max_score)
    
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get the result for each test case
result = max_score(T, test_cases)

# Print the results
for res in result:
    print(res)
