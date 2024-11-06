# cook your dish here
def qualify_round(X, A, B):
    total_score = A * 1 + B * 2
    if total_score >= X:
        return "Qualify"
    else:
        return "NotQualify"

T = int(input())

for _ in range(T):
    X, A, B = map(int, input().split())
    result = qualify_round(X, A, B)
    print(result)