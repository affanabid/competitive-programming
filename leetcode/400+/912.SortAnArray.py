class Solution:
    def mergeSort(self, A, p, r):
        if p < r:
            q = (p+r) // 2
            self.mergeSort(A, p, q)
            self.mergeSort(A, q+1, r)
            self.merge(A, p, q, r)
        return A

    def merge(self, A, p, q, r):
        n1 = q - p + 1
        n2 = r - q

        L = [0] * (n1 + 1)
        R = [0] * (n2 + 1)

        for i in range(n1):
            L[i] = A[p+i]
        for i in range(n2):
            R[i] = A[q+i+1]

        L[n1] = float('inf')
        R[n2] = float('inf')
        
        i = j = 0

        for k in range(p, r+1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)