class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        count=0
        for x in range(len(nums)-1):
            if(count==0 and nums[x]<nums[x+1]):
                count=1
            if(count==0 and nums[x]>nums[x+1]):
                count=2
            if(count==2 and nums[x]<nums[x+1]):
                return False
            if(count==1 and nums[x]>nums[x+1]):
                return False
        return True
