# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    versions = [False, False, False, False, False, True, True, True, True, True]

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l < r:
            m = l + (r - l) // 2
            if isBadVersion(m) == True:
                r = m
            else:
                l = m + 1
        return m
