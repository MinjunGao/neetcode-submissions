class Solution {
public:
    int shortestPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        return bfs(grid, 0, 0, m, n);
    }

private:
    int getPosition(int r, int c, int n) {
        return r * n + c;
    }

    int bfs(vector<vector<int>>& grid, int r, int c, int m, int n) {
        unordered_set<int> visited;
        queue<int> q;
        visited.insert(getPosition(r, c, n));
        q.push(getPosition(r, c, n));
        int distance = 0;
        while (!q.empty()) {
            int s = q.size();
            for (int i = 0; i < s; ++i) {
                int position = q.front();
                q.pop();
                int curr_r = position / n;
                int curr_c = position % n;
                if (curr_r == m - 1 && curr_c == n - 1) {
                    return distance;
                }
                vector<int> delta_r = {1, -1, 0, 0};
                vector<int> delta_c = {0, 0, 1, -1};
                for (int i = 0; i < 4; ++i) {
                    int new_r = curr_r + delta_r[i];
                    int new_c = curr_c + delta_c[i];
                    if (min(new_r, new_c) < 0 || new_r >= m || new_c >= n) {
                        continue;
                    }
                    if (grid[new_r][new_c] == 1) {
                        continue;
                    }
                    if (visited.find(getPosition(new_r, new_c, n)) != visited.end()) {
                        continue;
                    }
                    visited.insert(getPosition(new_r, new_c, n));
                    q.push(getPosition(new_r, new_c, n));
                }
            }
            ++distance;
        }
        return -1;
    }
};
