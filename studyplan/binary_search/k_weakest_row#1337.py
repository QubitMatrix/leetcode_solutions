class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr=[]
        arr1=[]
        for x in range(len(mat)):
            arr1.append((x,sum(mat[x])))
        arr1.sort(key= lambda x:x[1])
        print(arr1)

        for x in range(k):
            arr.append(arr1[x][0])
        return arr
