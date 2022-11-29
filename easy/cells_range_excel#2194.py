class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start_let=s[0]
        stop_let=s[3]
        start_num=s[1]
        stop_num=s[4]
        ss=""
        arr=[]
        for x in range(ord(start_let),ord(stop_let)+1,1):
            for y in range(ord(start_num),ord(stop_num)+1,1):
                ss=chr(x)+chr(y)
                arr.append(ss)
        return arr
