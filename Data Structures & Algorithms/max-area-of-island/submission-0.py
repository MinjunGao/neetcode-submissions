class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        res = 0

        m, n = len(grid), len(grid[0])
        visited = set() # (x, y)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                res = max(res, self.traverse(grid, visited, r, c, m, n))
        
        return res
    
    def traverse(self, grid, visited, r, c, m, n):
        if r < 0 or c < 0 or r == m or c == n:
            return 0
        if grid[r][c] == 0:
            return 0
        if (r, c) in visited:
            return 0
        visited.add((r, c))

        area = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            area += self.traverse(grid, visited, r + dr, c + dc, m, n)
        return area + 1