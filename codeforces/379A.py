def sol(a, b):
    hrs = a
    while a > 0:
        hrs += 1
        a = a//b
    print(hrs)

a, b = map(int, input().split())
sol(a, b)
