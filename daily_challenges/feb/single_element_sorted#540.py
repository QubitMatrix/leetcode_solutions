class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor=nums[0]
        for x in nums[1:]:
            xor=xor^x
        return xor
