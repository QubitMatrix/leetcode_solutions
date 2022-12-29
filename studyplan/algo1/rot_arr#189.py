class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(k==0 or k%len(nums)==0):
            return
        k=k%len(nums)
        t=nums[k*-1:]
        for x in range(len(nums)-1,k-1,-1):
            nums[x]=nums[x-k]
        nums[:k]=t
