# cook your dish here
def find_third_number(A, B):
  

    third_number = 21 - A - B
    return third_number if 1 <= third_number <= 10 else -1

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        result = find_third_number(A, B)
        print(result)