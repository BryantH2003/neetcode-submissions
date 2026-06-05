class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)
        
        for left in range(len(nums)):
            middle = left + 1
            right = len(nums) - 1

            while middle < right:
                if nums[left] + nums[middle] + nums[right] == 0:
                    if [nums[left],nums[middle],nums[right]] not in res:
                        res.append([nums[left],nums[middle],nums[right]])
                    middle += 1
                elif nums[left] + nums[middle] + nums[right] > 0:
                    right -= 1
                else:
                    middle += 1
        
        return res