class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        overallmax=curmax=nums[0]
        for i in range(1,len(nums)):
            curmax=max(curmax+nums[i],nums[i])
            if(curmax>overallmax):
                overallmax=curmax 
        return overallmax
