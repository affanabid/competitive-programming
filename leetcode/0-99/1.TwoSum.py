class Solution:
    def twoSum(self, nums, target):
        nums2 = sorted(nums)
        i = 0
        n = len(nums2) -1
        while i < n:
            sm = nums2[i] + nums2[n]
            if sm == target:
                i = nums.index(nums2[i])
                nums[i] = -1
                n = nums.index(nums2[n])
                return i, n

            elif sm > target:
                n -= 1
            elif sm < target:
                i += 1
            
