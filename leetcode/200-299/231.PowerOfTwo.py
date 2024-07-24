class Solution:
    def helper_rec(self, i, n):
        if i == n:
            return True
        if i > n:
            return False
        
        return self.helper_rec(i*2, n)
    def isPowerOfTwo(self, n: int) -> bool:
        return self.helper_rec(1, n)