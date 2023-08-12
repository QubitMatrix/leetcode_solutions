class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s=set()
        for x,y in ranges:
            s.update(set(range(x,y+1)))
        for x in range(left,right+1):
            if x not in s:
                return False
        return True
