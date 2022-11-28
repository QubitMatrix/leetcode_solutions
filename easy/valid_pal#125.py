class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for x in s:
            if(x.isalnum()):
                s1+=x
        s1=s1.lower()
        print(s1)
        if(s1==s1[::-1]):
            return True
        else:
            return False
