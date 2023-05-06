class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=-1
        j=-1
        for x in range(len(nums)-1,0,-1):
            if(nums[x]>nums[x-1]):
                i=x-1
                break
        if(i==-1):
            nums[:]=list(reversed(nums))
        else:
            for x in range(len(nums)-1,i-1,-1):
                if(nums[x]>nums[i]):
                    j=x
                    break
            nums[i],nums[j]=nums[j],nums[i]
            nums[i+1:]=list(reversed(nums[i+1:]))
