class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(strs)
        n = len(strs[0])

        for col in range(n):
            for row in range(1, m):
                curr, prev = strs[row], strs[row - 1]
                if col >= len(curr) or col >= len(prev) or curr[col] != prev[col]:
                    return strs[row][:col]
        
        return strs[0]
