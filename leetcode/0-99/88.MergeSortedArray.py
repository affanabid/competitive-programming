class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        numsC = nums1[::1]
        pointer = 0
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n and pointer < (m+n):
            if numsC[p1] == nums2[p2]:
                nums1[pointer] = numsC[p1]
                nums1[pointer+1] = nums2[p2]
                pointer += 2
                p1 += 1
                p2 += 1
            elif numsC[p1] < nums2[p2]:
                nums1[pointer] = numsC[p1]
                pointer += 1
                p1 += 1
            elif numsC[p1] > nums2[p2]:
                nums1[pointer] = nums2[p2]
                pointer += 1
                p2 += 1
        if p1 < m:
            while p1 < m:
                nums1[pointer] = numsC[p1]
                pointer += 1
                p1 += 1
        if p2 < n:
            while p2 < n:
                nums1[pointer] = nums2[p2]
                pointer += 1
                p2 += 1
        return nums1
