class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        arr=[]
        for x in target:
            a=s.count(x)
            b=target.count(x)
            c=a//b
            arr.append(c)
        return min(arr)
