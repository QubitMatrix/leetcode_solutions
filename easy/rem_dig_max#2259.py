class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        count=number.count(digit)
        pos=-1
        maxnum=0
        for x in range(count):
            pos=number.index(digit,pos+1)
            string=number[0:pos]+number[pos+1:]
            print(string,pos)
            if(int(string)>maxnum):
                maxnum=int(string)
        return str(maxnum)
