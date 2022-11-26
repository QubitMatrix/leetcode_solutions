class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip(" ")
        l=s.split(" ")
        print(s,l)
        return len(l[-1])
