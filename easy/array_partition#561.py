class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum1=0
        for x in range(0,len(nums),2):
            sum1+=nums[x]
        return sum1
