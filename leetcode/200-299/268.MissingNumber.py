class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n+1):
            ans ^= i

        for num in nums:
            ans ^= num

        return ans

# Approach Two
class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        expected = 0
        actual = 0
        for i in range(1, n+1):
            expected += i
        for num in nums:
            actual += num
        ans = expected - actual
        return ans