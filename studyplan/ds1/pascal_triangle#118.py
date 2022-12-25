class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[]
        for x in range(0,numRows):
            arr.append([1])
            for y in range(1,x):
                arr[x].append(arr[x-1][y-1]+arr[x-1][y])
            if(x!=0):
                arr[x].append(1)
        return arr
