from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        colChoicesToEqRows = defaultdict(int)
        for row in matrix:
            zeroCols = [str(i) for i, val in enumerate(row) if val == 0]
            oneCols = [str(i) for i, val in enumerate(row) if val == 1]
            colChoicesToEqRows[''.join(zeroCols)] += 1
            colChoicesToEqRows[''.join(oneCols)] += 1
        
        return max(rows for rows in colChoicesToEqRows.values())