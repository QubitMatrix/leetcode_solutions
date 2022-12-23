class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set([x for x in range(len(nums)+1)])-set(nums))[0]
