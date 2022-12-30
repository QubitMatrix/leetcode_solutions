class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for x in range(len(words)):
            for y in range(x+1,len(words)):
                for z in range(len(words[x])):
                    if(z>=len(words[y])):
                        return False
                    if(words[x][z]!=words[y][z]):
                        if(order.index(words[x][z])>order.index(words[y][z])):
                            return False
                        else:
                            break
        return True
