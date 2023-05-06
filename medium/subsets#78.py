class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        ans=[]
        for x in range(2**len(nums)):
            for y in range(len(nums)):
                if(x & 1<<y):
                    l.append(nums[y])
            ans.append(l)
            l=[]
        return ans
