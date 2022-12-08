class Solution:
    def minOperations(self, logs: List[str]) -> int:
        arr=[]
        for x in logs:
            if(x=="./"):
                continue
            elif(x=="../"):
                if(len(arr)!=0):
                    arr.pop()
            else:
                arr.append(x[:-1])
        return len(arr)
