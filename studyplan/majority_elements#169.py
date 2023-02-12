class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        maj=n//2
        for x in set(nums):
            if(nums.count(x)>maj):
                return int(x)
