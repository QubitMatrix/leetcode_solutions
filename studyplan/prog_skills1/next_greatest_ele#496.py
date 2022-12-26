class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for x in range(len(nums1)):
            y=nums2.index(nums1[x])
            if(y==-1):
                arr.append(-1)
            else:
                a=-1
                t=nums2[y+1:]
                for z in t:
                    if (z>nums1[x]):
                        a=z
                        break
                arr.append(a)
        return arr
