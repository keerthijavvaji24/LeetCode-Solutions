class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        for i in ransomNote:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        d2={}
        for i in magazine:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        for i in  ransomNote:
            if i in d2 and d2[i]>=d1[i]:
                continue
            else:
                return False
        else:
            return True

