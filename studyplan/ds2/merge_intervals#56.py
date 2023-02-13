class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        x=1
        while(x<len(intervals)):
            if(intervals[x][0]<=intervals[x-1][1]):
                intervals[x-1][1]=max(intervals[x][1],intervals[x-1][1])
                intervals.pop(x)
            else:
                x+=1
        return intervals
