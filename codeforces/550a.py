def sol(s):
    count = 2
    i = 0
    status1 = True
    status2 = True
    while i < len(s) - 1:
        if s[i] == 'A' and status1:
            if s[i+1] == 'B':
                status1 = False
                count -= 1
                i += 1
        elif s[i] == 'B' and status2:
            if s[i+1] == 'A':
                status2 = False
                count -= 1
                i += 1
        i += 1
    if count <= 0:
        return 'YES'
    else:
        return 'NO'

s = input()
print(sol(s))