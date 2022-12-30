class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
        """without using built-in:
        s1=""
        for x in s:
            if(ord(x)>=65 and ord(x)<=90):
                s1+=chr(ord(x)-ord('A')+ord('a'))
            else:
                s1+=x
        return s1
        """
