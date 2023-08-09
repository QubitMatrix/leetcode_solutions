class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum=[]
        prefix_sum.append(nums[0])
        for x in range(1,len(nums)):
            prefix_sum.append(prefix_sum[x-1]+nums[x])

        return prefix_sum
