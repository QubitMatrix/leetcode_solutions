import math
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg=0
        for x in nums:
            if(x==0):
                return 0
            elif(math.fabs(x)!=x):
                neg+=1
        if(neg%2==0):
            return 1
        else:
            return -1
