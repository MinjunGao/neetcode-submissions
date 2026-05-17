class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                idx = stk[-1][1]
                res[idx] = i - idx
                stk.pop()
            stk.append((t, i))
        
        return res