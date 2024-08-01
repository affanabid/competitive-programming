class Solution:
    def removeDuplicates(self, nums):
        seen = set()
        numsc = nums[::1]
        n = len(numsc)
        i = 0
        placer = 0
        k = 0
        while i < n:
            if numsc[i] not in seen:
                k += 1
                seen.add(numsc[i])
                nums[placer] = numsc[i]
                placer += 1
            i += 1
        return k

