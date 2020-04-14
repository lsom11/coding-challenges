class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move_left = 0
        length_of_string = len(s)
        for direction, amount in shift:
            if direction == 0:
                move_left = move_left + amount
            else:
                move_left -= amount
        move_left = move_left % length_of_string
        return s[move_left:] + s[:move_left]