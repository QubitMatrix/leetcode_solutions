class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic=defaultdict(int)
        for x in nums:
            dic[x]+=1
        r=dic[0]
        w=dic[1]
        b=dic[2]
        nums[0:r]=[0]*r
        nums[r:r+w]=[1]*w
        nums[r+w:]=[2]*b
