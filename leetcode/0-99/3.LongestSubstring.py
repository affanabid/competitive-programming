class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        hashmap = {}

        for end in range(len(s)):
            current = s[end]

            if current in hashmap:
                start = max(start, hashmap[current] + 1)

            hashmap[current] = end
            max_length = max(max_length, end - start + 1)

        return max_length