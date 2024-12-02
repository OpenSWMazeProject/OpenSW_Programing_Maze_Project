import random
import numpy as np

#prim 알고리즘을 사용하여 미로 생성
def generator(grid_size):
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    visited = []
    s = set()
    x, y = (0, 0)
    grid[x][y] = 1
    visited.append((x, y, grid[x][y]))
    fs = frontier(x, y, grid, grid_size)
    for f in fs:
        s.add(f)
    while s:
        x, y = random.choice(tuple(s))
        s.remove((x, y))
        ns = neighbours(x, y, grid, grid_size)
        if ns:
            nx, ny = random.choice(tuple(ns))
            connect(x, y, nx, ny, grid, visited)
        fs = frontier(x, y, grid, grid_size)
        for f in fs:
            s.add(f)
            
    return visited
            
def frontier(x, y, grid, grid_size):
    f = set()
    if x >= 0 and x < grid_size and y >= 0 and y < grid_size:
        if x > 1 and not grid[x-2][y]:
            f.add((x-2, y))
        if x + 2 < grid_size and not grid[x+2][y]:
            f.add((x+2, y))
        if y > 1 and not grid[x][y-2]:
            f.add((x, y-2))
        if y + 2 < grid_size and not grid[x][y+2]:
             f.add((x, y+2))    
    return f
    
def neighbours(x, y, grid, grid_size):
    n = set()
    if x >= 0 and x < grid_size and y >= 0 and y < grid_size:
        if x > 1 and grid[x-2][y]:
            n.add((x-2, y))
        if x + 2 < grid_size and grid[x+2][y]:
            n.add((x+2, y))
        if y > 1 and grid[x][y-2]:
            n.add((x, y-2))
        if y + 2 < grid_size and grid[x][y+2]:
            n.add((x, y+2))

    return n
        
def connect(x1, y1, x2, y2, grid, visited):
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    grid[x1][y1] = 1
    visited.append((x1, y1, grid[x1][y1]))
    grid[x][y] = 1
    visited.append((x, y, grid[x][y]))
    
if __name__ == "__main__" :
    grid_size = 21
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    generator(grid, grid_size)
    
    for row in grid:
        print(' '.join(['#' if cell == 0 else ' ' for cell in row]))

