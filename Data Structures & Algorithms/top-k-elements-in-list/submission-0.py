class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        min_heap = []
        for num in count.keys():
            heapq.heappush(min_heap, (count[num], num))
            if len(min_heap) > k: heapq.heappop(min_heap)
        
        res = []
        for freq, num in min_heap:
            res.append(num)
        return res