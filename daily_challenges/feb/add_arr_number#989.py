class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num1=0
        for x in range(len(num)):
            num1=num1*10+num[x]
        num1=num1+k
        l=map(lambda x:int(x),list(str(num1)))
        return(list(l))
