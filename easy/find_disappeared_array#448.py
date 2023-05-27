from collections import defaultdict
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic=defaultdict(int)
        arr=[]
        for x in nums:
            dic[x]+=1
        for x in range(1,len(nums)+1):
            if(dic[x]==0):
                arr.append(x)
        return arr
