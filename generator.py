
import random

def generate_maze(grid, x, y):
    # 가능한 방향 (상, 하, 좌, 우)
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)  # 방향을 무작위로 섞음

    for dx, dy in directions:
        nx, ny = x + dx, y + dy  # 이동할 새로운 위치

        # 새로운 위치가 grid 범위 내에 있는지 확인
        if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] == 0:
            grid[nx][ny] = 1  # 새로운 위치를 방문함
            grid[x + dx // 2][y + dy // 2] = 1  # 현재 위치와 새로운 위치 사이의 벽 제거
            generate_maze(grid, nx, ny)  # 재귀 호출로 다음 셀 탐색

def create_maze(grid):
    #grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    grid[0][0] = 1  # 시작 위치를 방문함
    generate_maze(grid, 0, 0)  # 미로 생성 시작
    return grid

# 예시 사용
#grid_size = 21  # 홀수 크기로 설정
#maze = create_maze(grid_size)

# 미로 출력
'''
for row in maze:
    print(' '.join(['#' if cell == 0 else ' ' for cell in row]))
'''
