import sys

while True:
    n = int(input())
    for i in range(n):
        data = input().split()
        print(int(data[0]) + int(data[1]), end='')
        if i <= n - 1:
            print("\n")
