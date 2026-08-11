class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # def multiply(n,nums):
        #     total=1
        #     for i in range(len(nums)):
        #         if i!=n:
        #             total*=nums[i]
        #         else:continue
        #     return( total)
        # l=[]
        # for i in range(len(nums)):
        #     l.append(multiply(i,nums))
        # return l 
        l=[1]*len(nums)
        # l[0]=1
        for i in range(1,len(nums)):
            l[i]=l[i-1]*nums[i-1]
        l2=[1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            l2[i]=l2[i+1]*nums[i+1]
        for i in range(len(l)):
            l[i]=l[i]*l2[i]
        return l

    
                


        