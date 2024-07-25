class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        gn = len(g)
        sn = len(s)
        i = j = out = 0
        while i < gn and j < sn:
            if s[j] >= g[i]:
                out += 1
                i += 1
                j += 1
            else:
                j += 1
        return out
