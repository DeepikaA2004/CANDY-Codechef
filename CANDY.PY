T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the number of candies
    N = int(input())

    # Check if N is divisible by 3
    if N % 3 == 0:
        print("YES")
    else:
        print("NO")