class Solution:
    def Game24Points(self, a):
        symbols = ['+', '-', '*', '/']
        for sym1 in symbols:
            for sym2 in symbols:
                for sym3 in symbols:
                    express = str(a[0]) + sym1 + str(a[1]) + sym2 + str(a[2]) + sym3 + str(a[3])
                    if eval(express) == 24:
                        return True

        return False
