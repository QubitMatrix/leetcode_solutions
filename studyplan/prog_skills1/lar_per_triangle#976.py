class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        total=0
        nums.sort()
        for x in range(len(nums)-2):
            if(nums[x]+nums[x+1]>nums[x+2]):
                tot=nums[x]+nums[x+1]+nums[x+2]
                if(tot>total):
                    total=tot
        return total
