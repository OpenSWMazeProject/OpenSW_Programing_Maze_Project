import random

def solver(maze, start, end):
    n, m = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = []
    path = []
    x, y = start

    while (x, y) != end:
        if (x, y) not in visited:
            visited.append((x, y))
            path.append((x, y))

        possible_moves = [(x + dx, y + dy) for dx, dy in directions if 0 <= x + dx < n and 0 <= y + dy < m and maze[x + dx][y + dy] == 1]
        
        if not possible_moves:
            break

        x, y = random.choice(possible_moves)

    path.append((x, y))
    return visited, path

if __name__ == "__main__":
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
