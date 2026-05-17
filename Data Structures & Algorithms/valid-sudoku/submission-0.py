class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                num = board[r][c]
                square_idx = (r // 3, c // 3)
                if num in rows[r] or num in cols[c] or num in squares[square_idx]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[square_idx].add(num)
        
        return True