class Solution:
    def validPalindrome(self, s: str) -> bool:
        for x in range(len(s)//2):
            s1=s
            if(s[x]!=s[len(s)-1-x]):
                s=s[:len(s)-1-x]+s[len(s)-1-x+1:]
                if(s=="".join(reversed(s))):
                    return True
                else:
                    s=s1
                    s1=s1[:x]+s1[x+1:]
                    if(s1=="".join(reversed(s1))):
                        return True
                    else:
                        return False
        return True
