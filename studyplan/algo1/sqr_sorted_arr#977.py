class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[x*-1 if x<0 else x for x in nums ]
        l.sort()
        l=map(lambda x:x**2,l)
        return l
