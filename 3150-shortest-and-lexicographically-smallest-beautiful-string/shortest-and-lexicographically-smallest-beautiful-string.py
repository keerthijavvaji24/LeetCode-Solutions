class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        m=float("INF")
        b=""
        ans=""
        for i in range(len(s)):
            c=0
            b=""
            for j in range(i,len(s)):
                b+=s[j]
                print(b)
                if s[j]=="1":
                    c+=1
                if c==k:
                    if len(b) < m or (len(b) == m and b < ans):
                        m=len(b)
                        ans=b
                    break
        return ans
        