class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s=set()
        s1=""
        mor=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for x in words:
            s1=""
            for y in x:
                pos=ord(y)-ord('a')
                s1+=mor[pos]
            s.add(s1)
        return len(s)
