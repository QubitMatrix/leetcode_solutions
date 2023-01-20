import itertools
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        s=[]
        flag=0
        l=list(range(len(nums)))
        for x in range(2,len(nums)+1):
            permutations=itertools.combinations(l,x)
            for y in permutations:
                s=[nums[y[0]]]
                for z in range(1,len(y)):
                    s.append(nums[y[z]])
                    if(nums[y[z]]<nums[y[z-1]]):
                        flag=1
                        break
                if(flag):
                    s=[]
                    flag=0
                    continue
                if(s not in arr):
                    arr.append(s)
                s=[]

        return arr
