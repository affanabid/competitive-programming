class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine:
                idx = magazine.index(char)
                magazine = magazine[:idx] + magazine[idx+1:]
            else:
                return False
        return True
