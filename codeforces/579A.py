def calc(lim):
    n  = 1
    while True:
        if n == lim:
            return (True, 0)
        if n > lim:
            n = n >> 1
            rem = lim - n
            return (False, rem)
        else:
            n = n << 1

def sol(lim):
    count = 1
    res = calc(lim)
    while True:
        
        if res[0]:
            return count
        else:
            res = calc(res[1])
            count += 1

x = int(input())
print(sol(x))

