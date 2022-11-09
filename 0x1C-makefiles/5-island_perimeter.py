#!/usr/bin/python3
"""5-island_perimeter.py"""


def islandPerimeter(self, grid: List[List[int]]) -> int:
    v = [[0, 0]]
    q = [[0, 0]]
    c = 0
    return self.bfs(grid, v, q, c)


def bfs(self, grid, v, q, c):
    if q == []:
        return c
    i = q[0][0]
    j = q[0][1]
    if grid[i][j]:
        c += 4
    if i-1 > -1:
        if [i-1, j] not in v:
            q.append([i-1, j])
            v.append([i-1, j])
        if grid[i-1][j] and grid[i][j]:
            c -= 1
    if j-1 > -1:
        if [i, j-1] not in v:
            q.append([i, j-1])
            v.append([i, j-1])
        if grid[i][j-1] and grid[i][j]:
            c -= 1
    try:
        a = grid[i+1][j]
        if [i+1, j] not in v:
            q.append([i+1, j])
            v.append([i+1, j])
        if grid[i+1][j] and grid[i][j]:
            c -= 1
    except:
        pass
    try:
        a = grid[i][j+1]
        if [i, j+1] not in v:
            q.append([i, j+1])
            v.append([i, j+1])
        if grid[i][j+1] and grid[i][j]:
            c -= 1
    except:
        pass
    del q[0]

    return self.bfs(grid, v, q, c)
