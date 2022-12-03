class Solution:
    def largestOddNumber(self, num: str) -> str:
        for x in range(len(num)-1,-1,-1):
            if(int(num[x])%2!=0):
                return num[:x+1]
        return ""
