class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans=[]
        for x in range(2**n):
            ans.append(x ^ x>>1)
        return ans
