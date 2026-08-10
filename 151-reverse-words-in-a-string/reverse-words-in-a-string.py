class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip().split()
        l=" ".join(s[::-1])
        return l


        