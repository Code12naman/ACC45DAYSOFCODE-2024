# cook your dish here
from collections import Counter

# Number of test cases
T = int(input())

for _ in range(T):
    # Read the number of cards
    N = int(input())
    
    # Read the list of numbers on the cards
    A = list(map(int, input().split()))
    
    # Count the frequency of each number
    freq = Counter(A)
    
    # Find the maximum frequency
    max_freq = max(freq.values())
    
    # The minimum moves are N - max_freq
    print(N - max_freq)
    