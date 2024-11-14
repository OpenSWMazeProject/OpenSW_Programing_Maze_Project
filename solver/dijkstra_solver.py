from collections import deque

def solver (maze, start, end) :
    n, m = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    visited = []
    queue = deque([(start[0], start[1], [])])
    
    while queue:
        x, y, path = queue.popleft()

        if (x, y) == end:
            path.append((x, y))
            return visited, path

        if x < 0 or y < 0 or x >= n or y >= m or maze[x][y] == 0 or (x, y) in visited:
            continue

        visited.append((x, y))
        new_path = path + [(x, y)]

        for dx, dy in directions:
            queue.append((x + dx, y + dy, new_path))

    return visited, []

if __name__ == "__main__" :
  

    # 미로 예시 (1은 통로, 0은 벽)
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

    # 시작, 끝
    start = (0, 0)
    end = (9, 9)

    visited, path = solver(maze, start, end)

    print("route:", visited)
    print("path:", path)
