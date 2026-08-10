class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []

        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > i:
                            l.append(nums2[k])
                            break
                    else:
                        l.append(-1)
                    break

        return l