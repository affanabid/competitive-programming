class Solution:
    def subsets(self, nums):
        result = []

        subset = []

        def depthFirstSearch(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            depthFirstSearch(i + 1)

            # do not include nums[i]
            subset.pop()
            depthFirstSearch(i + 1)

        depthFirstSearch(0)

        return result
