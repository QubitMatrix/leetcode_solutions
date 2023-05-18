class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        s=set()
        v=set(range(n))
        for x,y in edges:
            s.add(y)
        return list(v-s)
        
