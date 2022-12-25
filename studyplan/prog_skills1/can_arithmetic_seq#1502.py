class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d=arr[1]-arr[0]
        for x in range(len(arr)-1):
            if(arr[x+1]-arr[x]!=d):
                return False
        return True
