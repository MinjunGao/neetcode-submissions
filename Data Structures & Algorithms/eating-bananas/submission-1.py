class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            t = self.getTime(piles, mid)
            if t > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
        
    def getTime(self, piles, speed):
        t = 0
        for pile in piles:
            t += math.ceil(pile / speed)
        return t