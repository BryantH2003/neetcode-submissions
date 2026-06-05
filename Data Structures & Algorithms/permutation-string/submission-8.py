class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window = len(s1)
        sortedS1 = sorted(s1)
        left = 0
        
        while left < len(s2) - window:            
            if s2[left] in s1:
                right = left + window
                if sorted(s2[left:right]) == sortedS1:
                    return True
            left += 1
        
        if sorted(s2[left:]) == sortedS1:
            return True
        
        return False

        
