class Solution:
    def intToRoman(self, num: int) -> str:
        dic={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        val=[1000,500,100,50,10,5,1]
        exception={4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        s=""
        for x in range(len(val)):
            if(num==0):
                break
            num1=str(num)[0]+'0'*(len(str(num))-1)
            if(int(num1) in exception):
                num=num-int(num1)
                s+=exception[int(num1)]
            else:
                count=num//val[x]
                num=num%val[x]
                s+=dic[val[x]]*count
        return(s)
