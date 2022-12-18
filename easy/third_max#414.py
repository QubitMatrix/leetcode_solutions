class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        try:
            return nums[-3]
        except:
            return nums[-1]
