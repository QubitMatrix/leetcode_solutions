class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr2=[]
        arr3=[]
        for xx in arr:
            arr2.append((xx,int(math.fabs(x-xx))))
        arr2.sort(key=lambda x:x[1])
        arr2=arr2[:k]
        arr2.sort()
        for xx in arr2:
            arr3.append(xx[0])
        print(arr3)
        return arr3
