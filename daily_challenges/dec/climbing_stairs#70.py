class Solution:
    def climbStairs(self, n: int) -> int:
        count=0
        for i in range(n//2,-1,-1):
            num_one=(n-2*i)
            count+=math.factorial(num_one+i)/(math.factorial(num_one)*math.factorial(i))
        print(count)
        return int(count)
