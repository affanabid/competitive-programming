class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for char in s:
            asc = ord(char)
            if asc >= 65 and asc <= 90:
                newChar = chr(asc+32)
                newS += newChar
            elif asc >= 97 and asc <= 122:
                newS += char
            elif asc >= 48 and asc <= 57:
                newS += char
        n = len(newS) - 1
        i = 0
        while i <= n:
            if newS[i] != newS[n]:
                return False
            i += 1
            n -= 1
        return True

s = Solution()
print(s.isPalindrome('0p'))