s = input()

seen = set()
count = 0
for char in s:
    if char not in seen:
        seen.add(char)
        count += 1

if count % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

