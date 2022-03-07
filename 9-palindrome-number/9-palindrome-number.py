class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        s = list(str(x))
        
        if list(str(x)) == list(str(x))[::-1]:
            return True
        
        return False