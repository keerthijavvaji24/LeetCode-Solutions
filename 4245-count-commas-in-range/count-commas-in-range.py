class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        elif n>=1000 and n<100000:
            return n-1000+1
        else:
            return n-100000+99000+1

        