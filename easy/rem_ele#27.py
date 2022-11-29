class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         try:
                while(1):
                    nums.remove(val)
         finally:
            return len(nums)
