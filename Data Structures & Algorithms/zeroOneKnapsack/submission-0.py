class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity

        cache = [[-1] * (n + 1) for _ in range(m)]

        return self.dfs(0, profit, weight, capacity, cache)
    
    def dfs(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0
        if cache[i][capacity] != -1:
            return cache[i][capacity]
        
        cache[i][capacity] = self.dfs(i + 1, profit, weight, capacity, cache)

        new_capacity = capacity - weight[i]
        if new_capacity >= 0:
            p = profit[i] + self.dfs(i + 1, profit, weight, new_capacity, cache)
            cache[i][capacity] = max(cache[i][capacity], p)
        
        return cache[i][capacity]