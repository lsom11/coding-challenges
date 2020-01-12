class Solution:
    def isToeplitzMatrix(self, matrix):
        prev = []
        result = True
        # loop throw each row
        for row in matrix:
            # if prev row, verify if item is same as -1 of last row
            if len(prev):
                for i in range(1,len(row)):
                    if row[i] != prev[i-1]:
                        return False
            
            prev = row
        
        return result