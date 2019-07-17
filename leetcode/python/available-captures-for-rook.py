class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        capture = 0
        rookindex = None
        rookrow = None

        for row in board:
            if "R" in row:
                rookindex = row.index("R")
                rookrow = board.index(row)

        toprows = board[:rookrow]
        bottomrows = board[rookrow+1:]
        left = board[rookrow][:rookindex]
        right = board[rookrow][rookindex+1:]

        for x in right:
            if "." != x and "p" != x:
                break
            elif "p" == x:
                capture += 1
                break
        for x in reversed(left):
                if "." != x and "p" != x:
                    break
                elif "p" == x:
                    capture += 1
                    break

        topcapture = False
        for row in toprows:
            if row[rookindex] == "p" and not topcapture:
                capture += 1
                topcapture = True
            elif row[rookindex] != "." and row[rookindex] != "p":
                if capture >= 1 and topcapture:
                    capture -= 1
                    break

        bottomcapture = False
        for row in bottomrows:
            if row[rookindex] == "p" and not bottomcapture:
                capture += 1
                bottomcapture = True
            elif row[rookindex] != ".":
                break
        return capture
