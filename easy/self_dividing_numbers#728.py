class Solution:
    def check_num(self,num):
        if('0' in str(num)):
            return False
        else:
            for x in str(num):
                if(num%int(x)):
                    return False
            return True         
        
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr=[]
        for x in range(left,right+1):
            if(self.check_num(x)):
                arr.append(x)
        return arr
