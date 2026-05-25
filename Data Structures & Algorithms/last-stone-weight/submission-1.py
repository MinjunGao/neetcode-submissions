class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = [-stone for stone in stones]
        heapq.heapify(min_heap)

        while len(min_heap) > 1:
            a, b = heapq.heappop(min_heap), heapq.heappop(min_heap)
            heapq.heappush(min_heap, -abs(a - b))
        
        return -min_heap[0]