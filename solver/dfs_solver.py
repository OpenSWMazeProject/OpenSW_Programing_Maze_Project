#import matplotlib.pyplot as plt #시각화
import time

#미로 시각화 함수
'''
def draw_maze(maze, path=None, visited=None, delay=0.2):
    plt.imshow(maze, cmap='binary')  
    n, m = len(maze), len(maze[0])


    if visited:
        for x, y in visited:
            plt.plot(y, x, 'bo')  

    # 경로 표시
    if path:
        for x, y in path:
            plt.plot(y, x, 'go')  

    plt.draw()  
    plt.pause(delay)  
    plt.cla()  
'''

# DFS
def dfs_solver(maze, start, end):
    n, m = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    visited, path = [], []

    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= m or maze[x][y] == 0 or (x, y) in visited:
            return False
        
        visited.append((x, y))  
        # draw_maze(maze, path, visited) #시각화  

        if (x, y) == end:  
            path.append((x, y))
            return True

        for dx, dy in directions:  
            if dfs(x + dx, y + dy):
                path.append((x, y))
                return True
        
        return False
    
    #plt.figure(figsize=(6, 6)) #시각화  
    dfs(start[0], start[1])
    path.reverse() 
    #draw_maze(maze, path, visited) #시각화  
    #plt.show() #시각화
    
    return visited, path

# 미로 예시 (1은 통로, 0은 벽)
maze1 = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1]
]
maze = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
]

#시작, 끝
start = (0, 0)
end = (9, 9)

visited, path = dfs_solver(maze, start, end)

print("route", visited)
print("path:", path)