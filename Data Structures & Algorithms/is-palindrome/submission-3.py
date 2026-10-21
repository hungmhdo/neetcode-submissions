class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedText = "".join(char.lower() for char in s if char.isalnum())
        # n = len(cleanedText)
        # for i in range(n//2):
        #     if cleanedText[i] != cleanedText[n-i-1]:
        #         return False
        # return True
        return cleanedText == cleanedText[::-1]