class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        seen = {}
        string_map1 = ''
        pointer = 0
        for word in words:
            if word in seen:
                string_map1 += str(seen[word])
            else:
                seen[word] = pointer
                string_map1 += str(pointer)
                pointer += 1

        seen = {}
        string_map2 = ''
        pointer = 0
        for char in pattern:
            if char in seen:
                string_map2 += str(seen[char])
            else:
                seen[char] = pointer
                string_map2 += str(pointer)
                pointer += 1

        print(string_map1)
        print(string_map2)

                



sol = Solution()
p = 'abba'
s = 'dog cat cat dog'
sol.wordPattern(p, s)