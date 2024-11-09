import random

# Prim 알고리즘을 이용한 미로 생성 함수
def generater(grid, grid_size):
    # 미로의 초기 상태 (모든 벽을 '0'으로 설정)
    walls = []
    
    # 시작 지점 (0, 0)에서 벽을 추가
    grid[0][0] = 1  # 시작 위치를 통로로 설정
    add_walls(grid, 0, 0, walls, grid_size)
    
    while walls:
        # 벽 목록에서 무작위로 벽을 하나 선택
        wx, wy = random.choice(walls)
        walls.remove((wx, wy))
        
        # 벽이 두 개의 통로를 연결하는 경우, 벽을 제거하고 새 벽을 추가
        if is_valid_wall(grid, wx, wy, grid_size):
            grid[wx][wy] = 1  # 벽을 제거하고 통로로 변경
            add_walls(grid, wx, wy, walls, grid_size)

def add_walls(grid, x, y, walls, grid_size):
    # 주어진 좌표 (x, y)에서 4방향으로 벽을 추가
    for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx][ny] == 0:
            grid[x + dx // 2][y + dy // 2] = 1  # 현재 위치와 새로운 위치 사이의 벽 제거
            walls.append((nx, ny))

def is_valid_wall(grid, x, y, grid_size):
    # 벽이 두 개의 통로를 연결할 수 있는지 확인
    if grid[x][y] == 1:
        return False
    
    # 4방향으로 이미 통로가 있는지 확인
    count = 0
    for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx][ny] == 1:
            count += 1
    
    return count == 1

# 미로 출력 함수
def print_maze(grid):
    for row in grid:
        print(' '.join(['#' if cell == 0 else ' ' for cell in row]))

if __name__ == "__main__" :
    grid_size = 21  # 홀수 크기로 설정
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # 벽으로만 이루어진 그리드

    generater(grid, grid_size)  # Prim 알고리즘을 이용하여 미로 생성
    print_maze(grid)  # 미로 출력

