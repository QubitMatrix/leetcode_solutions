class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count=0
        z=0
        for x in arr1:
            for y in arr2:
                if(math.fabs(x-y)<=d):
                    z=1
                    break
            if(z==0):
                count+=1
            z=0
        return count
