class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if(coordinates[1][0]-coordinates[0][0]==0):
           s=-1
        else:
            s=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        for x in range(len(coordinates)-1):
            if(coordinates[x+1][0]-coordinates[x][0]==0):
                slope=-1
            else:
                slope=(coordinates[x+1][1]-coordinates[x][1])/(coordinates[x+1][0]-coordinates[x][0])
            if(s!=slope):
                return False
        return True
