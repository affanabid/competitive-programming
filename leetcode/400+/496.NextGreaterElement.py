class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    curr = nums2[j]
                    while j < len(nums2):
                        if nums2[j] > curr:
                            found = True
                            res.append(nums2[j])
                            break
                        j += 1
            if not found:
                res.append(-1)
        return res
                        

        