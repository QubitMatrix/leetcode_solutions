class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x=int(num**0.5)
        return(x**2==num)
