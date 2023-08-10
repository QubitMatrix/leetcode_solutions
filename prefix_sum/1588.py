class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefixsum=[arr[0]]
        s=sum(arr)
        for x in range(1,len(arr)):
            prefixsum.append(prefixsum[x-1]+arr[x])
        for x in range(len(arr)):
            for y in range(x+2,len(arr),2):
                s+=prefixsum[y]-prefixsum[x]+arr[x]
        return s
        
