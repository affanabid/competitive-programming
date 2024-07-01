def mergeSort(A, p, r):
    if p < r:
        q = (p+r)//2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1+1)
    R = [0] * (n2+1)
    for i in range(n1):
        L[i] = A[p + i]
    for i in range(n2):
        R[i] = A[q + i + 1]

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


def sol(n, shops, budget):
    start = 0
    end = n
    while start < end:
        mid = (start + end) // 2
        

def main():
    n = int(input())
    s = list(map(int, input().split()))
    mergeSort(s, 0, len(s) - 1) 

    d = int(input())
    for i in range(d):
        b = int(input())
        sol(n, s, b)

main()