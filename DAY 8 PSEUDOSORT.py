def is_pseudo_sorted(A, N):
    violations = 0
    violation_index = -1
    
    for i in range(N - 1):
        if A[i] > A[i + 1]:
            violations += 1
            violation_index = i
            if violations > 1:
                return "NO"
    
    if violations == 0:
        return "YES"
    
   
    if violations == 1:
        i = violation_index
       
        A[i], A[i + 1] = A[i + 1], A[i]
        
        for j in range(N - 1):
            if A[j] > A[j + 1]:
                return "NO"
        
        return "YES"
    

    return "NO"


T = int(input()) 

for _ in range(T):
    N = int(input())  
    A = list(map(int, input().split()))  
    
    result = is_pseudo_sorted(A, N)
    print(result)
