class Solution:
    def secondHighest(self, s: str) -> int:
        arr=[x for x in filter(lambda x:x.isnumeric(),s)]
        arr=list(set(arr))
        arr.sort()
        if(len(arr)<2):
            return -1
        return(int(arr[-2]))
