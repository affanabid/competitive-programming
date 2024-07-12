class Solution:
    def reverseBits(self, n: int) -> int:
        string = n[2:]
        stack = []
        for s in string:
            stack.append(s)
        ans = ''
        while stack:
            temp = stack.pop()
            ans += temp
        print(ans)
        self.toDecimal(string)

    def toDecimal(self, b):
        decimal = 0
        p = 0
        for bit in b:
            temp = int(bit) * (2 ** p)
            decimal += temp
            p += 1
        print(decimal)

s = Solution()
n = 32
n = bin(n)
s.reverseBits('00000010100101000001111010011100')
