class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)
                n = self.calc(n)
                print(n)


    def calc(self, n):
        n = str(n)
        ans = 0
        for i in n:
            ans += (int(i) ** 2)
        return ans

s = Solution()
s.isHappy(19)