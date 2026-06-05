class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * (len(nums))

        movingProd = 1

        for i in range(len(nums)-1,-1,-1):
            res[i] = movingProd
            movingProd *= nums[i]

        movingProd = 1

        for i in range(len(nums)):
            res[i] *= movingProd
            movingProd *= nums[i]

        return res
        
