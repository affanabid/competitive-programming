class Solution:
    def majorityElement(self, nums) -> int:
        nums.sort()
        return nums[len(nums)//2]