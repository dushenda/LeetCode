a = int(input())
address = []
for i in range(a):
    address.append(list(input().split()))
cnt = 1
for i in range(1, len(address)):
    if address[i - 1][1] != address[i][0]:
        cnt += 1
print(cnt)
