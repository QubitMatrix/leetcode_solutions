class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        minlen=1001
        arr=[]
        count=0
        for x in nums:
            len1=len(x)
            if(len1<minlen):
                minlen=len1
                minstr=x
        for x in range(minlen):
            for y in nums:
                if(minstr[x] not in y):
                    count=1
            if(count==1):
                count=0
            else:
                arr.append(minstr[x])
        arr.sort()
        return arr
