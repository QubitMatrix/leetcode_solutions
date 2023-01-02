class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=""
        count=0
        for x in range(len(s)):
            if(s[x] not in s1):
                s1+=s[x]
            else:
                count=max(count,len(s1))
                s1=s1[s1.index(s[x])+1:]+s[x]
        count=max(count,len(s1))
        return count
