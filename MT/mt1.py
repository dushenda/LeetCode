def get_reverse_num(a):
    return int(str(a)[::-1])


a = int(input())
cnt = 0
res = []
for i in range(1, a // 4 + 1):
    if i * 4 == get_reverse_num(i):
        cnt += 1
        res.append([i, 4 * i])

print(cnt)
for iv in res:
    print(iv[0], iv[1])
