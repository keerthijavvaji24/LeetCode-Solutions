class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = list(set(nums))
        s.sort()
        c = 0
        l = []

        for i in range(len(s) - 1):
            if s[i + 1] - s[i] == 1:
                c += 1
            else:
                l.append(c + 1)  
                c = 0
        l.append(c + 1)

        return max(l)