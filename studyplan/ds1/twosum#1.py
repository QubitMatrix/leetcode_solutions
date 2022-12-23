class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[(pos,x) for pos,x in enumerate(nums)]
        arr.sort(key=lambda x:x[1])
        print(arr)
        mid=0+len(nums)//2
        l=0
        h=len(nums)
        for x in range(len(nums)):
            l=0
            h=len(nums)
            while(l<=h):
                mid=(l+h)//2
                print(mid)
                if(mid>=len(nums)):
                    break
                if(arr[mid][1]+arr[x][1]==target and arr[mid][0]!=arr[x][0]):
                    return list((arr[mid][0],arr[x][0]))
                elif(arr[mid][1]+arr[x][1]<target):
                    l=mid+1
                else:
                    h=mid-1
