class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr=[]
        s1=""
        count=0
        for x in s:
            if(x.isalpha()):
                arr.append(x)
        arr.reverse()
        for x in s:
            if(x.isalpha()):
                s1+=arr[count]
                count+=1
            else:
                s1+=x
        return s1
