class SummaryRanges:

    def __init__(self):
        self.arr=[]
        self.dic={}

    def addNum(self, value: int) -> None:
        dic=self.dic
        arr=self.arr
        
        if(value not in dic):
            if(value+1 in dic and value-1 not in dic):
                arr[dic[value+1]][0]=value
                dic[value]=dic[value+1]
            elif (value-1 in dic and value+1 not in dic):
                arr[dic[value-1]][1]=value
                dic[value]=dic[value-1]
            elif(value+1 in dic and value-1 in dic and dic[value+1]!=dic[value-1]):
                
                arr[dic[value-1]][1]=arr[dic[value+1]][1]
                arr[dic[value+1]]=[-1,-1]
                for z in range(arr[dic[value-1]][0],arr[dic[value-1]][1]+1):
                    dic[z]=dic[value-1]

            else:
                dic[value]=len(arr)
                arr.append([value,value])
            
    def getIntervals(self) -> List[List[int]]:
            arr=[[x,y] for x,y in self.arr if y!=-1 and x!=-1]
            arr.sort(key=lambda x:x[0])
            return(arr)
            
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
