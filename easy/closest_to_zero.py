class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        xx=100001
        yy=-100001
        for x in range(len(nums)):
            if(nums[x]<0):
                yy=nums[x]
            elif(nums[x]>=0):
                xx=nums[x]
                break
        if(xx>math.fabs(yy)):
            return yy
        else:
            return xx
