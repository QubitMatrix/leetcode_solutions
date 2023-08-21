class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1=""
        s_=set()
        for x in s:
            if(x in s_ and len(s)%len(s1)==0 and s1*(len(s)//len(s1))==s):
                return True
            s1+=x
            s_.add(x)
        return False
