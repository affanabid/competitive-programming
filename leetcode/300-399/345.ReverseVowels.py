class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        i = 0
        n = len(s) - 1
        newS = list(s)
        while i < n:
            if s[i] in vowels and s[n] in vowels:
                temp = newS[i]
                newS[i] = newS[n]
                newS[n] = temp
                i += 1
                n -= 1
            if newS[i] not in vowels:
                i += 1
            if newS[n] not in vowels:
                n -= 1
        s = ''
        for char in newS:
            s += char
        return s 
