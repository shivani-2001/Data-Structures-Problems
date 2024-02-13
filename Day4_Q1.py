# Question - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Method 1 ->
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in box[(i//3, j//3)]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                box[(i//3, j//3)].add(board[i][j])

        return True
