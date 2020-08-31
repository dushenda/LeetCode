while True:
    a = int(input())
    if a == 0:
        break
    list1 = list(map(int, input().split()))
    for i in range(1, sum(list1) + 1):
        if sum(list1) % i == 0 and (i > max(list1)):
            print(i)
            break
