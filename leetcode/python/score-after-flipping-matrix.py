class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row_num = len(A)
        col_num = len(A[0])
        
        for i in range(row_num):
            this_row = A[i]
            if this_row[0] == 1:
                continue
            #flip this row
            for j in range (col_num):
                if this_row[j] == 1:
                    this_row[j] = 0
                else:
                    this_row[j] = 1
            A[i] = this_row
            
   
        for j in range (col_num):
            one_total = 0
            for i in range (row_num):
                if A[i][j] == 1:
                    one_total += 1
            if one_total > row_num / 2:
                continue
            
            #flip this col
            for i in range (row_num):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
        
        
        
        level = 1
        total = 0
        for j in range (col_num - 1, -1, -1):
            one_total = 0
            for i in range (row_num):
                if A[i][j] == 1:
                    one_total += 1
            total += one_total * level
            level *= 2
        
        return total