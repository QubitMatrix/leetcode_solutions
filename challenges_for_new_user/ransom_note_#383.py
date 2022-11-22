class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print(set(ransomNote).intersection(set(magazine)),set(magazine))
        if(set(ransomNote).intersection(set(magazine))!=set(ransomNote)):
            print("1")
            return False
        else:
            for x in magazine:
                if(ransomNote.count(x)>magazine.count(x)):
                    return False
            return True
