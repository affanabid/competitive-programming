class Solution:
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


sol = Solution()
arr = [4,5,6,7,0,1,2]
print(sol.findMin(arr))