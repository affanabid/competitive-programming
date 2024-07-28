class Solution:
    def groupAnagrams(self, strs):
        seen = {}
        for s in strs:
            so = "".join(sorted(s))
            if so not in seen:
                seen[so] = [s]
            else:
                seen[so].append(s)
        return seen.values() 