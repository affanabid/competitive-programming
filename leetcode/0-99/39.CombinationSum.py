class Solution:
    def combinationSum(self, candidates, target: int):
        result = []

        def depthFirstSearch(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            depthFirstSearch(i, curr, total + candidates[i])

            curr.pop() 
            depthFirstSearch(i+1, curr, total)

        depthFirstSearch(0, [], 0)

        return result