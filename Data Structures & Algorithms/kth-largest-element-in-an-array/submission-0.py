class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [-num for num in nums]
        heapq.heapify(min_heap)

        for _ in range(k - 1):
            heapq.heappop(min_heap)
        
        return -heapq.heappop(min_heap)