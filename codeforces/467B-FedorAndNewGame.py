def friends(players, fedor, n, m, k):
    friend = 0
    for player in players:
        diff = differingBits(player, fedor)
        count = 0
        for d in diff:
            if d == '1':
                count += 1
        if count <= k:
            friend += 1
    print((friend))
 
def differingBits(n1, n2):
    result = n1 ^ n2
    result = bin(result)[2:].zfill(8)
    return result
 
n, m, k = map(int,input().split())
players = []
for i in range(m+1):
    player = int(input())
    players.append(player)
 
fedor = players.pop()
friends(players, fedor, n, m, k)
 
 
# print(bin(5)[2:].zfill(8))