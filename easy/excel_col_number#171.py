class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count=0
        sums=0
        columnTitle="".join(reversed(columnTitle))
        for x in columnTitle:
            sums+=(ord(x)-64)*(26**count)
            count+=1
        return sums
