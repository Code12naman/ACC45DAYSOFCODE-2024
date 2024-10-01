# cook your dish here
from collections import Counter

def min_operations_to_make_elements_same(test_cases):
    results = []
    for case in test_cases:
        N, A = case
        frequency = Counter(A) 
        max_frequency = max(frequency.values())  
        results.append(N - max_frequency) 
    return results


T = int(input())  
test_cases = []
for _ in range(T):
    N = int(input())  
    A = list(map(int, input().split()))  
    test_cases.append((N, A))

results = min_operations_to_make_elements_same(test_cases)

for result in results:
    print(result)
