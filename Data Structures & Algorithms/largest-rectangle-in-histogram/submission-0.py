class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stk = [] # pair (idx, height)
        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                idx, height = stk.pop()
                start = idx
                width = i - idx
                area = width * height
                res = max(res, area)
            stk.append((start, h))
        
        for i, h in stk:
            width = len(heights) - i
            height = h
            area = width * height
            res = max(res, area)

        return res
