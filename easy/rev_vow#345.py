count=0
class Solution:
    def reverseVowels(self, s: str) -> str:
        '''global count
        count+=1
        if(count==478)://to check the specific case inputs
            raise SyntaxError'''
        counter=0
        let=[]
        s1=""
        vow={'a','A','e','E','i','I','o','O','u','U'}
        for x in range(len(s)):
            if(s[x] in vow):
                let.append(s[x])
        let.reverse()
        for x in range(len(s)):
            if(s[x] in vow):
                s1+=let[counter]
                counter+=1
            else:
                s1+=s[x]
        return s1
