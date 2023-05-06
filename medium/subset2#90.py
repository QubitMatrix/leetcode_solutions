class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        l=[]
        for x in range(2**len(nums)):
            for y in range(len(nums)):
                if(x & 1<<y):
                    l.append(nums[y])
            ans.add(tuple(sorted(l)))
            l=[]
        return ans
