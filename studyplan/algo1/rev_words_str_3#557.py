class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        ss=""
        for x in s:
            ss+=x[::-1]+" "
        return ss[:-1]
