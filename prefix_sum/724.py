class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum={}
        prefix_sum[0]=nums[0]
        for x in range(1,len(nums)):
            prefix_sum[x]=prefix_sum[x-1]+nums[x]
        if(prefix_sum[len(nums)-1]-prefix_sum[0]==0):
            return 0
        for x in range(1,len(nums)):
            if(prefix_sum[x-1]==prefix_sum[len(nums)-1]-prefix_sum[x]):
                return x
        return -1
