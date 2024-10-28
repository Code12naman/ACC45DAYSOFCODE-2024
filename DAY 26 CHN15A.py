
def count_wolverine_minions(N, K, characteristics):
    count = 0
    for value in characteristics:
        mutated_value = value + K
        if mutated_value % 7 == 0:
            count += 1
    return count

T = int(input())  

for _ in range(T):
  
    N, K = map(int, input().split())
    
 
    characteristics = list(map(int, input().split()))
    
   
    result = count_wolverine_minions(N, K, characteristics)
    print(result)
    