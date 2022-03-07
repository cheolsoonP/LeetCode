class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        s = list(str(x))
        
        if s == s[::-1]:
            return True
        
        return False