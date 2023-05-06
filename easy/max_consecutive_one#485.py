class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxval=0
        nums.append(0) #sentinel
        for  x in range(len(nums)):
            if(nums[x]==0):
                if(maxval<count):
                    maxval=count
                count=0
            else:
                count+=1
        return maxval
