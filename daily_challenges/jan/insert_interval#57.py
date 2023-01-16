class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr=[]
        flag=0
        pos=0
        end=newInterval[1]
        for s,e in intervals:
            if(flag==0 and e>=newInterval[0]):
                start=min(s,newInterval[0])
                start_pos=pos
                flag=1
            if(flag==1 and s<=newInterval[1]):
                end=max(e,newInterval[1])
            elif(flag==1 and s>newInterval[1]):
                arr.extend(intervals[0:start_pos])
                arr.append([start,end])
                arr.extend(intervals[pos:])
                flag=2
                break
            pos+=1
        if(flag==0):
            intervals.append(newInterval)
            return intervals
        if(flag==1):
            arr.extend(intervals[0:start_pos])
            arr.append([start,end])
        return arr
