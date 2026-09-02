class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                n = board[r][c]

                if n == ".":
                    continue

                box = (r // 3) * 3 + c // 3

                if n in rows[r] or n in cols[c] or n in boxes[box]:
                    return False

                rows[r].add(n)
                cols[c].add(n)
                boxes[box].add(n)

        return True
