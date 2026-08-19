class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=str(n)
        p,c=1,0
        for i in s:
            p*=int(i)
            c+=int(i)
        return p-c
        