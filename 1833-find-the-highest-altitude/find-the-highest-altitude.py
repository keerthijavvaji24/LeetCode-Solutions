class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0,0)
        s=0
        l=[]
        m=0
        # print(gain)
        for i in gain:
            s+=i
            m=max(m,s)
            l.append(s)
        print(l)
        return m
        