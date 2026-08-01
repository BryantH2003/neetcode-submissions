class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def backtrack(perm, nums, pickedNums):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for i in range(len(nums)):
                if not pickedNums[i]:
                    perm.append(nums[i])
                    pickedNums[i] = True
                    backtrack(perm,nums,pickedNums)
                    perm.pop()
                    pickedNums[i] = False

        result = []
        pickedNums = [False] * len(nums)
        backtrack([], nums, pickedNums)

        return result