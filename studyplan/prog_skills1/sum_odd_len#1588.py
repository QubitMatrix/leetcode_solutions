class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total=0
        sum1=0
        for x in range(1,len(arr)+1,2):
            for y in range(0,len(arr)-x+1):
                t=arr[y:y+x]
                sum1=sum(t)
                total+=sum1
        return total
