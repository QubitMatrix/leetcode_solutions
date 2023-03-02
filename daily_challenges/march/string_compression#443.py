class Solution:
    def compress(self, chars: List[str]) -> int:
        arr=[]
        count=0
        cur=chars[0]
        for x in chars:
            if(x==cur):
                count+=1
            else:
                arr.append(cur)
                if(count!=1):
                    arr.extend(list(str(count)))
                count=1
                cur=x
        arr.append(cur)
        if(count!=1):
            arr.extend(list(str(count)))
        chars[0:len(arr)]=arr
        return len(arr)
