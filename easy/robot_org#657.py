class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up=left=0
        for x in moves:
            if(x=='U'):
                up+=1
            elif(x=='D'):
                up-=1
            elif(x=='L'):
                left+=1
            else:
                left-=1
        return (up==0 and left==0)
