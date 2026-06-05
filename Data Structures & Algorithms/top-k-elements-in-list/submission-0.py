class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Heap
        
        dct = {}
        heap = []

        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1
        
        for num in dct.keys():
            heapq.heappush(heap, (dct[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

