class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        msb = s[0]
        if msb == '-':
            sign = -1
            s = s[1:]
        else:
            sign = 1
        st = []
        for c in s:
            st.append(c)
        n = ''
        while st:
            n += st.pop()

        # n = s[::-1]
        
        result = sign * int(n)
        ub = (2 ** 31) - 1
        lb = -(2 ** 31)
        if result > lb and result < ub:
            return result
        else:
            return 0

s = [1,2,3,4,5]
print(s[::-1])