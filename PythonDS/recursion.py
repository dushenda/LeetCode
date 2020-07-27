def fib(n):
    # Fibonacci更好的递归
    if n <= 1:
        return n, 0
    else:
        a, b = fib(n - 1)
    return a + b, a


def reverse(S, start, end):
    # 原地换数
    if start < end:
        reverse(S, start + 1, end - 1)
        S[start], S[end] = S[end], S[start]


def binary_sum(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


if __name__ == '__main__':
    ll = [1, 2, 3, 4]
    res = binary_sum(ll, 0, len(ll))
    print(res)
