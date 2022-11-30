class Solution:
    def checkRecord(self, s: str) -> bool:
        count=0
        if(s.count('A')>=2):
            return False
        else:
            for x in s:
                if(x=='L'):
                    count+=1
                else:
                    count=0
                if(count==3):
                    return False
            return True
