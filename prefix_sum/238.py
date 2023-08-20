class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        prev=post=1
        for x in range(n):
            ans[x]*=prev
            prev*=nums[x]
            ans[n-x-1]*=post
            post*=nums[n-x-1]
        return ans
        
