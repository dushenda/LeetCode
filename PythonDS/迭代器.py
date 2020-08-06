def fibon(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


f = fibon(1000)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))