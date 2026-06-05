class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        heatMap = {}

        for num in nums:
            if num not in heatMap:
                heatMap[num] = 1
            else:
                heatMap[num] += 1

        for num,count in heatMap.items():
            
            heap.append((count,num))

        heap.sort()
        print(heap)
        result = []

        for item in heap:
            result.append(item[1])

            if len(result) > k:
                result.pop(0)
            
        
        return result