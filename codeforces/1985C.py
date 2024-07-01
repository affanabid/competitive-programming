def sol(n, array):
    if n == 1 and array[0] == 0:
        print(1)
        return
    if n == 1 and array[0] != 0:
        print(0)
        return
    good = 0
    i = 1
    while i < n:
        curr = array[0:i]
        for k in range(len(curr)):
            curr_sum = 0
            for j in range(len(curr)):
                if k != j:
                    curr_sum += array[j]
            print(curr_sum)
            print(array[k])
            print()
            if curr_sum == array[k]:
                good += 1
                break
        i += 1
    print(good)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int, input().split()))
        sol(n, array)

sol(4, [1,1,2,0])
# array = [0,1,2,1]
# for i in range(len(array)):
#     curr_sum = 0
#     for j in range(len(array)):
#         if i != j:
#             curr_sum += array[j]
#     if curr_sum == array[i]:
#         print('good')
#         break
