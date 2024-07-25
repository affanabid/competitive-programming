class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0 
        n = len(s) - 1
        while i <= n:
            temp = s[i]
            s[i] = s[n]
            s[n] = temp
            i += 1
            n -= 1
        