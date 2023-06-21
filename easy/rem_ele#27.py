class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=j=0
        while(i<=j and j<len(nums)):
            if(nums[j]!=val):
                if(nums[i]==val):
                    nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
        return i
