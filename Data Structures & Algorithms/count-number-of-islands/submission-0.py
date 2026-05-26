class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        res = 0
        visited = set() # (x, y)

        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r, c) not in visited:
                    res += 1
                    self.traverse(grid, visited, r, c, m, n)
        
        return res
    
    def traverse(self, grid, visited, r, c, m, n):
        if r < 0 or r == m or c < 0 or c == n:
            return
        if grid[r][c] != '1':
            return
        if (r, c) in visited:
            return
        
        visited.add((r, c))
        self.traverse(grid, visited, r + 1, c, m, n)
        self.traverse(grid, visited, r - 1, c, m, n)
        self.traverse(grid, visited, r, c + 1, m, n)
        self.traverse(grid, visited, r, c - 1, m, n)
