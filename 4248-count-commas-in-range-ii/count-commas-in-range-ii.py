class Solution:
    def countCommas(self, n: int) -> int:
        a=0
        b=1000
        while b<=n:
            a+=(n-b+1)
            if n//1000<b:break
            b*=1000
        return a       