class Solution {
public:
    int countPaths(vector<vector<int>>& grid) {
        unordered_set<int> visited;
        return backtrack(grid, visited, 0, 0);
    }

private:
    int backtrack(vector<vector<int>>& grid, unordered_set<int>& visited, int r, int c) {
        if (min(r, c) < 0 || r >= grid.size() || c >= grid[0].size()) {
            return 0;
        }
        if (grid[r][c] == 1) {
            return 0;
        }
        int position = getPosition(grid.size(), r, c);
        if (visited.find(position) != visited.end()) {
            return 0;
        }
        if (r == grid.size() - 1 && c == grid[0].size() - 1) {
            return 1;
        }
        int count = 0;
        visited.insert(position);
        count += backtrack(grid, visited, r + 1, c);
        count += backtrack(grid, visited, r - 1, c);
        count += backtrack(grid, visited, r, c + 1);
        count += backtrack(grid, visited, r, c - 1);
        visited.erase(position);
        return count;
    }

    int getPosition(int ROW, int r, int c) {
        return r * ROW + c;
    }
};
