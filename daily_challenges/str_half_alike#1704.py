class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow=['a','A','e','E','i','I','o','O','u','U']
        count1=count2=0
        for x in range(len(s)//2):
            if(s[x] in vow):
                count1+=1
        for x in range(len(s)//2,len(s)):
            if(s[x] in vow):
                count2+=1
        return count1==count2
