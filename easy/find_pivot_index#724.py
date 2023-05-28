class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        prev_sum=0
        if(sum(nums[1:])==0):
            return 0
        for x in range(1,len(nums)):
            prev_sum+=nums[x-1]
            next_sum=total-prev_sum-nums[x]
            if(prev_sum==next_sum):
                return x
        return -1
