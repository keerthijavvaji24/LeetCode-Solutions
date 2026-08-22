class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        c, p = 0, 1
        for i in s:
            c += int(i)
            p *= int(i)
        return n % (c+p) == 0