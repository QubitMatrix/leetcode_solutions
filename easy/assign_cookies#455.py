class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        count=0
        x=0
        y=0
        while(x<len(s) and y<len(g)):
            if(s[x]>=g[y]):
                count+=1
                y+=1
                x+=1
            else:
                y+=1
        return count
