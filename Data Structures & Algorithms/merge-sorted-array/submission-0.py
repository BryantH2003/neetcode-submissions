class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 3 pointer 
        
        writePtr = m + n - 1
        left = m - 1
        right = n - 1

        while left >= 0 and right >= 0:
            if nums2[right] >= nums1[left]:
                nums1[writePtr] = nums2[right]
                right -= 1
            else:
                nums1[writePtr] = nums1[left]
                left -= 1
            
            writePtr -= 1
        
        while left >= 0:
            nums1[writePtr] = nums1[left]
            left -= 1
            writePtr -= 1
        
        while right >= 0:
            nums1[writePtr] = nums2[right]
            right -= 1
            writePtr -= 1
        
        return nums1