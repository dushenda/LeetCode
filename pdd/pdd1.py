K, N = list(map(int, input().split()))
D = list(map(int, input().split()))
x = 0
cnt = 0
flg = 0
if K != 0:
    for i in range(N):
        x += D[i]
        if x > K:
            x = K - (x - K)
            cnt += 1
        elif x == K:
            flg = 1
            print("paradox")
            break
    if flg == 0:
        print(str(K - x) + ' ' + str(cnt))
else:
    print("paradox")
