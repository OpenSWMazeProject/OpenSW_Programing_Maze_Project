import random

def generator(grid_size):
    visited = []
    rows = 21
    cols = 21
    index = 2

    grid = [[1 for _ in range(rows)] for _ in range(rows)]

    for i in range(1, rows, 2):
        for j in range(1, cols, 2):
            grid[i][j] = 0

    for i in range(grid_size):
        for j in range(grid_size):
            visited.append((i, j, grid[i][j]))

    for j in range(0, cols, 2):
        grid[0][j] = index
        visited.append((0, j, grid[0][j]))
        index += 1

    for i in range(0, rows, 2):
        for j in range(0, cols - 2, 2):
            if random.choice([True, False]):
                grid[i][j + 1] = 0
                visited.append((i, j + 1, grid[i][j + 1]))
            else:
                if grid[i][j] == grid[i][j + 2]:
                    grid[i][j + 1] = 0
                    visited.append((i, j + 1, grid[i][j + 1]))
                else:
                    target = grid[i][j + 2]
                    for k in range(0, cols, 2):
                        if grid[i][k] == target:
                            grid[i][k] = grid[i][j]
                            visited.append((i, k, grid[i][k]))

        for j in range(0, cols, 2):
            if i != rows - 1:
                grid[i + 2][j] = grid[i][j]
                visited.append((i + 2, j, grid[i + 2][j]))

                if random.choice([True, False]):
                    temp = grid[i][j]
                    count = sum(1 for z in range(0, cols, 2) if grid[i][z] == temp and grid[i + 1][z] == 1)
                    if count > 1:
                        grid[i + 1][j] = 0
                        visited.append((i + 1, j, grid[i + 1][j]))
                        grid[i + 2][j] = index
                        visited.append((i + 2, j, grid[i + 2][j]))
                        index += 1

    for j in range(0, cols - 2, 2):
        if grid[rows - 1][j] != grid[rows - 1][j + 2]:
            grid[rows - 1][j+1] = 1
            visited.append((rows - 1, j+1, grid[rows - 1][j+1]))
            temp = grid[rows - 1][j + 2]


            for z in range(0, cols, 2):
                if grid[rows - 1][z] == temp:
                    grid[rows - 1][z] = grid[rows - 1][j]
                    visited.append((rows - 1, z, grid[rows - 1][z]))

    for i in range(0, rows, 2):
        for j in range(0, cols, 2):
            grid[i][j] = 1
            visited.append((i, j, grid[i][j]))


    return visited
    
if __name__ == "__main__" :

    # 예시 사용
    grid_size = 21  # 홀수 크기로 설정
    maze = generator(grid_size)

    # 미로 출력

    for row in maze:
        print(' '.join(['#' if cell == 0 else ' ' for cell in row]))
