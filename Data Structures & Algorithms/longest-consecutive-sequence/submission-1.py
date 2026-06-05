class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        count = 1
        relMax = 0

        for num in nums:
            if num + 1 not in nums:
                relMax = num - 1
                while relMax in nums:
                    count += 1
                    relMax -= 1
                res = max(res,count)
                count = 1
        
        return res