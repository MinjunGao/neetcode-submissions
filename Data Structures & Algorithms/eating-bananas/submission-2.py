class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2
            t = self.getTime(piles, mid)
            if t > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        
        return res
        
    def getTime(self, piles, speed):
        t = 0
        for pile in piles:
            t += math.ceil(pile / speed)
        return t