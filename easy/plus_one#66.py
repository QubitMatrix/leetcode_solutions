class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int("".join(map(str,digits)))
        return(list(map(int,str(num+1))))
        
