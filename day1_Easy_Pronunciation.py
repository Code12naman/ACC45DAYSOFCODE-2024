
def is_easy_to_pronounce(S):
    vowels = set('aeiou')
    consecutive_consonants = 0
    
    for char in S:
        if char not in vowels:  
            consecutive_consonants += 1
            if consecutive_consonants >= 4:
                return "NO"
        else:  
            consecutive_consonants = 0
    
    return "YES"

def main():
    T = int(input())  
    for _ in range(T):
        N = int(input())  
        S = input().strip()  
        print(is_easy_to_pronounce(S))


if __name__ == "__main__":
    main()
