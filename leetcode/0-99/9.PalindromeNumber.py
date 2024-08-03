class Solution:
    def isPalindrome(self, x: int) -> bool:        
        def pal(s):
            if len(s) == 0:
                return True
            if s[0] != s[-1]:
                return False
            return pal(s[1:-1])
        x = str(x)
        return pal(x)