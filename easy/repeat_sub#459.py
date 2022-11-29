class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub=""
        for x in s:
                sub+=x
                if(len(s)%len(sub)==0 and sub!=s):
                    if(sub*(len(s)//len(sub))==s):
                        return True
        return False
