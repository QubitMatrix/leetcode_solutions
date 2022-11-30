class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        l=[1 for x in stones if(x in jewels)]
        return len(l)
