def is_sys(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def has_sys(s, m):
    for i in range(len(s) - m):
        if is_sys(s[i:i + m]):
            return True
    return False


N = int(input())
for i in range(N):
    n, m = list(map(int, input().split()))
    s = str(input())
    if has_sys(s, m):
        print("YES")
    else:
        print("NO")
