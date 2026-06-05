class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = []
        heap = []

        for i in range(len(position)):
            heap.append((position[i],speed[i]))

        heap.sort(reverse=True)
        
        for pos,speed in heap:
            res.append((target - pos) / speed)
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()
        
        return len(res)

            