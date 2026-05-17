class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def backtrack(visited, r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS:
                return 0
            if grid[r][c] == 1:
                return 0
            if (r, c) in visited:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            count = 0
            visited.add((r, c))
            count += backtrack(visited, r + 1, c)
            count += backtrack(visited, r - 1, c)
            count += backtrack(visited, r, c + 1)
            count += backtrack(visited, r, c - 1)
            visited.remove((r, c))
            return count
        return backtrack(set(), 0, 0)