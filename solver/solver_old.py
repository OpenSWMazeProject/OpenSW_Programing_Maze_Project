import matplotlib.pyplot as plt
import time


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

# DFS
def dfs_with_visualization(maze):
    n, m = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    visited, path = [], []

    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= m or maze[x][y] == 0 or (x, y) in visited:
            return False
        
        visited.append((x, y))  
        draw_maze(maze, path, visited)  

        if x == n-1 and y == m-1:  
            path.append((x, y))
            return True

        for dx, dy in directions:  
            if dfs(x + dx, y + dy):
                path.append((x, y))
                return True
        
        return False
    
    plt.figure(figsize=(6, 6))  #
    dfs(0, 0)
    path.reverse()  # 경로를 올바른 순서로 정렬
    draw_maze(maze, path, visited)  
    plt.show()
    
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

# 미로 탐색 실행 및 시각화
visited, path = dfs_with_visualization(maze)

# 방문한 경로와 최종 경로 출력
print("route:", visited)
print("path:", path)