class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr=[]
        r1=0
        c1=0
        if(len(mat)*len(mat[0])==r*c):
            for x in range(r):
                arr.append([])
                for y in range(c):
                    if(c1==len(mat[0])):
                        c1=0
                        r1+=1
                    print(mat[r1][c1])
                    arr[x].append(mat[r1][c1])
                    c1+=1
            return arr
        else:
            return mat
