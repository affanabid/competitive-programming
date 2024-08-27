def sol(s):
    count = 2
    i = 0
    while i < len(s) - 1:
        if s[i] == 'A':
            if s[i+1] == 'B':
                count -= 1
                i += 1
        elif s[i] == 'B':
            if s[i+1] == 'A':
                count -= 1
                i += 1
        i += 1
    if count == 0:
        return 'YES'
    else:
        return 'NO'

s = input()
print(sol(s))