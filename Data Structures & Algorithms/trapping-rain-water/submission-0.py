class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        l_max = [0] * n
        l_max[0] = height[0]
        r_max = [0] * n
        r_max[-1] = height[-1]

        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i - 1])
        for i in range(n - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])
        
        for i in range(n):
            res += min(l_max[i], r_max[i]) - height[i]
        
        return res