class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s="balloon"
        arr=[]
        for x in s:
            a=s.count(x)
            b=text.count(x)
            c=b//a
            arr.append(c)
        return min(arr)
