# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys


def f(line1, line2):
    ln = int(line1)
    nums = list(line2.split(' '))
    nums = [int(i) for i in nums]
    target = nums[-1]
    res = 0
    for v in nums[-1::-1]:
        if v == target:
            res += 1
        else:
            break
    res1, res2 = 0, 0
    if res // 2 == 1:
        res1 += 1
    else:
        res2 += 1
    if res1 > res2:
        print("NIUNIU")
    else:
        print("NIUMEI")


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line1 = sys.stdin.readline().strip()
        line2 = sys.stdin.readline().strip()
        f(line1, line2)
