class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1,d2={},{}
        if len(s)!=len(t):return False
        for i in range(len(s)):
            if s[i] in d1 :
                if  d1[s[i]]!=t[i]:
                    return False
                else:continue
            else:
                d1[s[i]]=t[i]

            if t[i] in d2 :
                if d2[t[i]]!=s[i]:
                    return False
                else:
                    continue
            else:
                d2[t[i]]=s[i]
        return True



          

