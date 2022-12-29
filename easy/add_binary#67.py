class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ad=int(a,2)
        bd=int(b,2)
        cd=ad+bd
        c=bin(cd).replace('0b',"")
        return(c)
