class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while(len(str1)!=len(str2)):
            if(len(str1)>len(str2)):
                if(str1[len(str2)*-1:]==str2):
                    str1=str1[0:len(str2)*-1]
                else:
                    break

            elif(len(str2)>len(str1)):
                if(str2[len(str1)*-1:]==str1):
                    str2=str2[0:len(str1)*-1]

        return str1 if str1==str2 else ""
