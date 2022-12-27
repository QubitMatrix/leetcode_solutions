class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        count=0
        arr=[]
        for x in range(len(capacity)):
            d=capacity[x]-rocks[x]
            if(d==0):
                count+=1
            else:
                arr.append(d)
        arr.sort()
        for x in arr:
            if(additionalRocks>=x):
                additionalRocks-=x
                count+=1
            else:
                break
        return count
