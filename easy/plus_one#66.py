class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if(digits[-1]!=9):
            digits[-1]+=1
        else:
            i=len(digits)-1
            while(i>-2):
                if(i==-1):
                    temp=digits.copy()
                    digits=[]
                    digits.append(1)
                    digits.extend(temp)
                    break
                digits[i]+=1
                if(digits[i]==10):
                    digits[i]=0
                elif(digits[i]<10): 
                    break
                i-=1
        return digits
