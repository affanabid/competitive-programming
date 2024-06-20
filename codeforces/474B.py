def juicyWorms(n, worms, m, labels):
    ranges = []
    sum = 0
    for worm in worms:
        a = sum + 1
        b = sum + worm
        data = (a,b)
        ranges.append(data)
        sum += worm

    for i in range(m):
        curr = labels[i]
        i = 0
        j = n
        while i < j:
            mid = (i+j) // 2
            temp = ranges[mid]
            lb = temp[0]
            ub = temp[1]
            if curr >= lb and curr <= ub:
                print(mid + 1)
                break
            elif curr < lb:
                j = mid - 1
            elif curr > ub:
                i = mid + 1


n = int(input())
worms = list(map(int, input().split()))
m = int(input())
labels = list(map(int, input().split()))
# n = 5
# worms = [2,7,3,4,9]
# m = 3
# labels = [1,25,11]
juicyWorms(n, worms, m, labels)

