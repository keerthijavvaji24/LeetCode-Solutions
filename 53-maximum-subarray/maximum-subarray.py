class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        c_s=nums[0]
        m_s=nums[0]
        for i in range(1,len(nums)):
            c_s=max(nums[i],nums[i]+c_s)
            m_s=max(m_s,c_s)
        return m_s
