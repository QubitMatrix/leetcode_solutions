class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        h=len(arr)
        while(l<=h):
            mid=(l+h)//2
            if(mid>=len(arr)):
                break
            if(mid-1>=0 and mid+1<len(arr)):
                if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                    return mid
                elif(arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]):
                    l=mid+1
                elif(arr[mid]<arr[mid-1] and arr[mid]>arr[mid+1]):
                    h=mid-1
            elif(mid-1<0):
                l=mid+1
            elif(mid+1>=len(arr)):
                h=mid-1
                    
