class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pos=len(s)//2
        for x in range(pos):
            t=s[x]
            s[x]=s[(x+1)*-1]
            s[(x+1)*-1]=t
