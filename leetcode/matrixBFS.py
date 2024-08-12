from collections import deque as queue

rowD = [-1,0,1,0]
colD = [0,1,0,-1]

def ValidMove(visited, row, col):
    rLimit = 4
    cLimit = 4

    if row < 0 or col < 0 or row >= rLimit or col >= cLimit:
        return False
    
    if visited[row][col]:
        return False
    
    return True

def bfs(matrix, visited, row, col):

    q = queue()

    q.append((row,col))

    visited[row][col] = True

    while q:
        cell = q.popleft()
        x = cell[0]
        y = cell[1]

        print(matrix[x][y], end=' ')

        for i in range(4):
            adjx = x + rowD[i]
            adjy = y + colD[i]

            if ValidMove(visited, adjx, adjy):
                visited[adjx][adjy] = True
                q.append((adjx, adjy))


grid= [ [ 1, 2, 3, 4 ],
           [ 5, 6, 7, 8 ],
           [ 9, 10, 11, 12 ],
           [ 13, 14, 15, 16 ] ]
 
    # Declare the visited array
vis = [[ False for i in range(4)] for i in range(4)]
# vis, False, sizeof vis)

bfs(grid, vis, 0, 0)
        

