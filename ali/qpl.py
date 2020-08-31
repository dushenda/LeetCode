def permute(li):
    res = []

    def backtrace(li, temp):
        if not li:
            res.append(temp)
            return
        for i in range(len(li)):
            backtrace(li[0:i] + li[i + 1::], temp + [li[i]])

    backtrace(li, [])
    return res


if __name__ == '__main__':
    s = 'dingtalk'
    res = permute(list(s))
    print(res)
    for iv in res:
        print(''.join(iv))
