import matplotlib.pyplot as plt
import time

def draw_maze(maze, path=None, visited=None, delay=0.1):
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


def bfs_with_visualization(maze):
    n, m = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    visited, path = [], []

    def bfs(x, y):
        queue = [(x, y)]  
        visited.append((x, y))  
        draw_maze(maze, path, visited)  

        while queue:
            x, y = queue.pop(0)  
            if x == n-1 and y == m-1:  
                path.append((x, y))
                return True

            for dx, dy in directions:  
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m or maze[nx][ny] == 1 or (nx, ny) in visited:
                    continue

                visited.append((nx, ny))  
                path.append((x, y))  
                queue.append((nx, ny))  
                draw_maze(maze, path, visited)  

        return False



    plt.figure(figsize=(6, 6))  
    bfs(0, 0)
    draw_maze(maze, path, visited)  
    plt.show()

maze = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
]

bfs_with_visualization(maze)