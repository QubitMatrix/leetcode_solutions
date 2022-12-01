class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines=1
        wid=0
        res=[]
        for x in s:
            wid+=widths[ord(x)-ord('a')]
            if(wid>100):
                wid=widths[ord(x)-ord('a')]
                lines+=1
        res.append(lines)
        res.append(wid)
        return res
