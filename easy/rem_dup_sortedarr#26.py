class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        nums.clear()
        nums.extend(s)
        nums.sort()
        print(nums)
        return len(s)
