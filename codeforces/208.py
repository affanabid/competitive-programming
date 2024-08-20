s = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'

checker = 'WUB'
new_s = ''
n = len(s)
i = 0
complete = False
while i < n:
    if s[i] == checker[0]:
        temp = ''
        j = 0
        while i < n and j < 3 and s[i] == checker[j]:
            temp += checker[j]
            i += 1
            j += 1
        if j != 3:
            new_s += temp
        complete = True

    else:
        new_s += s[i]
        i += 1


print(new_s)