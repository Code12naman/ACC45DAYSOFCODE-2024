# cook your dish here
import math

def min_attacks(H, X, Y):
    # Option 1: Use only normal attacks
    option1 = math.ceil(H / X)
    
    # Option 2: Use the special attack once, then normal attacks
    if H <= Y:
        option2 = 1  # Special attack is enough
    else:
        option2 = 1 + math.ceil((H - Y) / X)
    
    # Return the minimum of the two options
    return min(option1, option2)

# Input reading and processing
T = int(input())  # Number of test cases
for _ in range(T):
    H, X, Y = map(int, input().split())
    result = min_attacks(H, X, Y)
    print(result)
