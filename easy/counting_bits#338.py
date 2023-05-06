class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]
        count=0
        for x in range(1,n+1):
            bits=math.floor(math.log(x,2))+1
            for y in range(bits):
                if(x & 1<<y):
                    count+=1
            ans.append(count)
            count=0
        return ans
