from collections import deque

def righthand_solver(maze, start, end):
    n, m = len(maze), len(maze[0])
    dir = 0 #이동할 방향 (0~3)
    directions = [(1,0), (0, -1), (-1, 0), (0, 1)] #나아가는 방향 (하,좌,상,우)
    hand_y = [0, -1, 0, 1]  #손을 대고 있는 방향(좌, 상, 우, 하)
    hand_x = [-1, 0, 1, 0]

    def turn(direction, rotate):  #이동방향, #회전할 방향(-1: 좌, 1: 우)
        fixed_dir = (direction + rotate + 4) % 4
        return fixed_dir

    queue = deque([(start[0], start[1], [])])
    while queue:
        y, x, visited = queue.popleft()

        if (y, x) == end: #완료지점 도착
            visited.append((y, x))
            return visited, set(visited)  #방문 한 횟수, 길

        hand = (y + hand_y[dir], x + hand_x[dir])   
        if 0 <= hand[0] < n and 0 <= hand[1] < m and maze[hand[0]][hand[1]] == 1: #우측 통로 확인
            dir = turn(dir, 1)    #우측 통로 있으면 우회전
            visited.append((y, x))
            queue.append([hand[0], hand[1], visited])
            continue
        
        front = (y + directions[dir][0], x + directions[dir][1]) 
        if 0 <= front[0] < n and 0 <= front[1] < m and maze[front[0]][front[1]] == 1: #전면 통로 확인
            visited.append((y, x))
            queue.append([front[0], front[1], visited])
            continue
        else:
            dir = turn(dir, -1)   # 길막히면 좌회전
            queue.append([y, x, visited])
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

    visited, path = righthand_solver(maze, start, end)

    print("route:", visited)
    print("path:", path)

    #test
    #test_maze = [[0] *10 for _ in range(10)]

    #for y, x in visited:
    #    test_maze[y][x] +=1
    #for i in range(0, 10):
    #    print(test_maze[i])
