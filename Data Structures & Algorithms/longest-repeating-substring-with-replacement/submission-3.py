class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        uniqueLetters = set(s)

        for letter in s:
            count = 0
            left = 0

            for right in range(len(s)):
                if s[right] == letter:
                    count += 1
                
                while (right - left + 1) - count > k:
                    if s[left] == letter:
                        count -= 1
                    left += 1
                
                res = max(res, right - left + 1)
        
        return res