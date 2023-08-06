class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsum=[]
        self.prefixsum.append(nums[0])
        for x in range(1,len(nums)):
            self.prefixsum.append(self.prefixsum[x-1]+nums[x]) 

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixsum[right]-self.prefixsum[left-1] if left!=0 else self.prefixsum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
