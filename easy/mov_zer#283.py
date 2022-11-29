class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        try:
            while(1):
                nums.remove(0)
        except:
            x=length-len(nums)
            nums.extend([0]*x)
