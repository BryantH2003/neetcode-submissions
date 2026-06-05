class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # You want me to return the indncies of two numbers such that they add up to the target
        # A number can not be used twice
        # Reutnr the answer with the sammer index first
        
        # Will there always be a solution?

        dct = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in dct:
                return [dct[diff], i]
            
            dct[nums[i]] = i
        
        return []