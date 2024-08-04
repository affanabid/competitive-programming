class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapp1 = [0] * 100
        pointer1 = 0
        s1 = ''
        mapp2 = [0] * 100
        pointer2 = 0
        s2 = ''
        for char in s:
            if char not in mapp1:
                mapp1[pointer1] = char
                s1 += ' '
                s1 += str(pointer1)
                pointer1 += 1
            else:
                s1 += ' '
                s1 += str(mapp1.index(char))

        for char in t:
            if char not in mapp2:
                mapp2[pointer2] = char
                s2 += ' '
                s2 += str(pointer2)
                pointer2 += 1
            else: 
                s2 += ' '
                s2 += str(mapp2.index(char))
        print(s1)
        print(s2)

        
        print(s1 == s2)
            

sol = Solution()
t = "add"
s = 'egg'
sol.isIsomorphic(s, t)


# Another optimal approach
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a1 = []
        a2 = []
        for char in s:
            a1.append(s.index(char))
        for char in t:
            a2.append(t.index(char))
        return a1 == a2
