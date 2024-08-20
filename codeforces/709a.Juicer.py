n, b, d = map(int, input().split())

oranges = list(map(int, input().split()))
count = 0
curr = 0
for orange in oranges:
    if orange <= b:
        curr += orange
        if curr > d:
            curr = 0
            count += 1

print(count)
