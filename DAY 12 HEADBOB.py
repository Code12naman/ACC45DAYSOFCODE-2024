# cook your dish here
# Number of test cases
T = int(input())

for _ in range(T):
    # Read number of gestures
    N = int(input())
    # Read the string of gestures
    gestures = input()

    if 'I' in gestures:
        print("INDIAN")
    elif 'Y' in gestures:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
        