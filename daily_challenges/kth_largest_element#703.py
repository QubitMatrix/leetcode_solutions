class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.nums.sort()
    def add(self, val: int) -> int:
        if(not self.nums):
            self.nums.append(val)
            return self.nums[-1*self.k]
        if(val<self.nums[0]):
            self.nums[1:]=self.nums[:]
            self.nums[0]=val
            return self.nums[-1*self.k]
        elif(val>self.nums[-1]):
            self.nums.append(val)
            return self.nums[-1*self.k]
        for x in range(len(self.nums)):
            if(val<=self.nums[x]):
                pos=x
                break
        self.nums[pos+1:]=self.nums[pos:]
        self.nums[pos]=val
        return self.nums[-1*self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
