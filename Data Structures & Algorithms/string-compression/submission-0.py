class Solution:
    def compress(self, chars: List[str]) -> int:
        # O(1) Space

        # Bein with empty sting s
        left = 0
        k = 0
        
        # For consecutive repeating characters in char
        while left < len(chars):
            chars[k] = chars[left]
            k += 1
            right = left + 1

            while right < len(chars) and chars[left] == chars[right]:
                right += 1
            
            if right - left > 1:
                # Converting int to string
                for c in str(right - left):
                    chars[k] = c
                    k += 1
            
            left = right
        
        return k
            # If group length is 1 --> append character to s

            # Else append character follow by group's length
        
        # s should be stored in array chars

        # k = length of compressed string s

        # return k