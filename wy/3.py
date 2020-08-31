import datetime

T = int(input())


def func():
    a2 = []
    time = []
    i = 0
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        return
    b = list(map(int, input().split()))
    while i < len(a):
        a2.append(a[i] + a[i + 1])
        i += 2

    for i in range(len(a2)):
        if a2[i] < b[i]:
            time.append(a2[i])
        else:
            time.append(b[i])
    print(sum(time))


def prt(add):
    time_origin = datetime.datetime(2020, 8, 20, 8, 0, 0)
    time_origin = time_origin + datetime.timedelta(minutes=add)
    print(time_origin.strftime("%H:%M:%S am"))


for i in range(T):
    prt(func())
