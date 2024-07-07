import math
class Solution:
#math.log(power, base)
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if math.log(n, 4).is_integer():
            return True
        return False