class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)
        while(l<=h):
            mid=(l+h)//2
            if(mid>=len(nums)):
                break
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                l=mid+1
            else:
                h=mid-1
        return -1
