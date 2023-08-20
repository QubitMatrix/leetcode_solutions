class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixproduct=[1]*len(nums)
        suffixproduct=[1]*len(nums)
        ans=[]
        for x in range(1,len(nums)):
            prefixproduct[x]=prefixproduct[x-1]*nums[x-1]
        for x in range(len(nums)-2,-1,-1):
            suffixproduct[x]=suffixproduct[x+1]*nums[x+1]
        for x in range (len(nums)):
            ans.append(prefixproduct[x]*suffixproduct[x])
        return ans
        
