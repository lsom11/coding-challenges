class Solution:
	#Slope Calculation : y2 - y1 /  x2 - x1
    def getSlope(self, del_y, del_x):
        if del_x == 0:
            slope = 9999
        else:
            slope = del_y / del_x
        return slope
    
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        del_y = coordinates[1][1] - coordinates[0][1] 
        del_x = coordinates[1][0] - coordinates[0][0]      
        slope = self.getSlope(del_y, del_x)
        for i in range(1, len(coordinates) - 1):
            del_y = coordinates[i + 1][1] - coordinates[i][1]
            del_x = coordinates[i + 1][0] - coordinates[i][0]
            slope2 = self.getSlope(del_y, del_x)
            
            if slope != slope2:
                return False
            else:
                return True
            