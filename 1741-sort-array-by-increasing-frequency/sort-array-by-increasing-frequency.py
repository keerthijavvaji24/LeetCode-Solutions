class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        d = {}
        l = []

        nums2 = nums.copy()

        # Step 1: Count frequencies
        for i in nums2:
            d[i] = d.get(i, 0) + 1

        f = 1
        while f <= len(nums):
            same_fre = []
            for i in d:
                if d[i] == f:
                    same_fre.append(i)
            same_fre.sort(reverse=True)
            for num in same_fre:
                for _ in range(f):
                    l.append(num)
            f += 1
        return l