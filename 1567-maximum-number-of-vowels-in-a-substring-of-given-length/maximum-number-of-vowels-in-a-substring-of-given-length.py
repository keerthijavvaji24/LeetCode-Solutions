class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l,c=0,0
        m=float("-inf")
        lst=[]
        for i in range(len(s)):
            if s[i] in "aeiou":
                c+=1
            if i-l+1==k:
                m=max(m,c)
                if s[l] in "aeiou":
                    c-=1
                l+=1
        return m