class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        res=sorted(d,key=d.get,reverse=True)
        return res[:k]

        