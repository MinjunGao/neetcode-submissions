class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        m, n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    self.traverse(grid, r, c, m, n, set())
        
    def traverse(self, grid, r, c, m, n, visited):
        visited.add((r, c))
        q = deque([(r, c)])
        distance = 0

        while q:
            sz = len(q)
            distance += 1
            for _ in range(sz):
                o_r, o_c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    n_r, n_c = o_r + dr, o_c + dc
                    if n_r < 0 or n_c < 0 or n_r == m or n_c == n:
                        continue
                    if (n_r, n_c) in visited:
                        continue
                    if grid[n_r][n_c] == 0 or grid[n_r][n_c] == -1:
                        continue
                    if grid[n_r][n_c] <= distance:
                        continue
                    grid[n_r][n_c] = distance
                    visited.add((n_r, n_c))
                    q.append((n_r, n_c))