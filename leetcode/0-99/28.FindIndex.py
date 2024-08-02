class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        needle = list(needle)
        needle = needle[::-1]
        for i in range(n):
            curr = i
            if haystack[i] == needle[-1]:
                needleCopy = needle[::1]
                while needleCopy and i < n:
                    temp = needleCopy.pop()
                    if temp != haystack[i]:
                        needleCopy.append(temp)
                        break
                    i += 1
                if not needleCopy:
                    return curr
        return -1


