class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        
        permutations = self.permute(nums[1:])

        result = []

        for perm in permutations:
            for i in range(len(perm) + 1):
                permCopy = perm.copy()
                permCopy.insert(i, nums[0])
                result.append(permCopy)

        return result
