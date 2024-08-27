def sol2(n, m, arr):
    tasks = m
    i = 1
    k = 0
    j = 0
    while True:
        if i == arr[j]:
            while i == arr[j]:
                tasks -= 1
                j += 1
                if j >= m:
                    break
            
        

        if tasks == 0:
            break
        i += 1
        k +=1
        if i > n:
            i = 1
    print(k)

#optimized approach
def sol(houses, noOfTasks, tasks):
    time = 0
    curr = 1
    for task in tasks:
        if curr <= task:
            time += task - curr
        else:
            time += houses - (curr - task)
        curr = task
    print(time)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
sol(n,m,arr)

