class Solution:
    def search(self, nums, target):
        mn = min(nums)
        min_index = nums.index(mn)
        if target == nums[min_index]:
            return min_index
        elif target > nums[-1]:
            left = 0
            right = min_index - 1
        else:
            left = min_index
            right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

