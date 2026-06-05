class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleanedString = ""

        for letter in s:
            if letter.isalnum():
                cleanedString += letter

        cleanedString = cleanedString.lower()

        print(cleanedString)
        
        left = 0
        right = len(cleanedString) - 1
        while left < right:
            if cleanedString[left] != cleanedString[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True