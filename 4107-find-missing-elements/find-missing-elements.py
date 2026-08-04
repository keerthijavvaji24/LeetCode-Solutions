class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=max(nums)
        n=min(nums)
        s=set(nums)
        l=[]
        for i in range(n,m):
            if i not in s:
                l.append(i)
        return l


        