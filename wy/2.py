n = int(input())
li = list(map(int, input().split()))
ans = [i//2 for i in li]
print(sum(ans))
