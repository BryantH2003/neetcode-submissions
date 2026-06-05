class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0

        for left in range(len(heights)):
            maxRight = 0
            right = len(heights) - 1
            
            while left < right:
                if heights[right] > maxRight:
                    maxRight = heights[right]

                    if heights[left] > maxRight:
                        res = max(res, maxRight*(right - left))
                    else:
                        res = max(res, heights[left]*(right - left))
                else:
                    right -= 1
        
        return res