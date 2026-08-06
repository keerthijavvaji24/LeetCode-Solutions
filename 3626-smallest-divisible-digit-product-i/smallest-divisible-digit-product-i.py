class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n!=0:
            n=str(n)
            pro=1
            for i in n:
                pro*=int(i)
            if pro%t==0:
                return int(n)
            else:n=str(int(n)+1)


        