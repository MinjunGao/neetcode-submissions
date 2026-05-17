class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stk = deque()
        res = []
        l = r = 0
        while r < len(nums):
            num_in = nums[r]
            while stk and stk[-1] < num_in:
                stk.pop()
            stk.append(num_in)
            r += 1
            if r - l == k:
                res.append(stk[0])
                if stk[0] == nums[l]:
                    stk.popleft()
                l += 1
        return res