class Solution:
    def is_valid(self, coordinates):
        return 0 <= coordinates[0] < 8 and 0 <= coordinates[1] < 8
    def queensAttacktheKing(self, queens, king):
        attacking_queens = {str(queen[0]) + str(queen[1]): False for queen in queens}
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for i in range(8):
            curr_coordinates = king
            curr_coordinates = [curr_coordinates[0] + directions[i][0], curr_coordinates[1] + directions[i][1]]
            while self.is_valid(curr_coordinates):
                queen = str(curr_coordinates[0]) + str(curr_coordinates[1])
                if queen in attacking_queens:
                    attacking_queens[queen] = True
                    break
                curr_coordinates = [curr_coordinates[0] + directions[i][0], curr_coordinates[1] + directions[i][1]]
        return [queen for queen in queens if attacking_queens[str(queen[0]) + str(queen[1])] == True]