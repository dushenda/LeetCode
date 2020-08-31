s = input()
k = int(input())
ret = 'z' * k
for i in range(len(s) - k):
    tmp = s[i:k]
    if ret>tmp: ret=tmp
print(ret)