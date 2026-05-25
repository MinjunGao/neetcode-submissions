class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [] # (distance, point)

        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(min_heap, (distance, (x, y)))
        
        res = []
        for _ in range(k):
            point = heapq.heappop(min_heap)[1]
            res.append(point)
        return res