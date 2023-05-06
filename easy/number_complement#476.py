class Solution:
    def findComplement(self, num: int) -> int:
        s=str(bin(num))[2:]
        print(s)
        ans=""
        for x in s:
            ans+=str(1-int(x))
        return int(ans,2)
