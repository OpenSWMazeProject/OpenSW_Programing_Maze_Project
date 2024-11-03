from collections import deque

def heuristic(p1, p2):    #휴리스틱 함수 h(x)
    return abs((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    #return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))

def a_star(maze, start, end):
    n, m = len(maze), len(maze[0])
    queue = deque([(0, start)])
    come_from = {}  # 경로 추적용 딕셔너리
    visited = []  #방문 추적용 배열
    g_score = {(0, 0): 0}  #g(x) 값
    f_score = {(0, 0): heuristic(start, end)} #f(x) = (g(x) +h(x)) 값
    
    while queue:
        current_f, current = min(queue, key=lambda x: x[0]) #f(x)값이 제일 낮은 노드 선택
        queue.remove((current_f, current))
        visited.append(current) #방문

        if current == end:  #도착시 방문지, 경로 출력
            path = []
            while current in come_from:
                path.append(current)
                current = come_from[current]
            path.append((0, 0))
            path.reverse()
            return visited, path

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  #방향 (우, 하, 좌, 상)
            neighbor = (current[0] + direction[0], current[1] + direction[1]) #이웃 노드
            if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and maze[neighbor[0]][neighbor[1]] == 1: #이웃노드 통로일시
                neighbor_g_score = g_score[current] + 1  #이웃노드 g(x)값 추가 
                if neighbor not in g_score or neighbor_g_score < g_score[neighbor]:  #g(x)값 최솟값으로
                    come_from[neighbor] = current #현재->이웃 경로 저장
                    g_score[neighbor] = neighbor_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end) #f(x) = g(x) + h(x)
                    queue.append((f_score[neighbor], neighbor)) 
    return visited, None

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

    visited, path = a_star(maze, start, end)

    print("route:", visited)
    print("path:", path)

    # test
    # test_maze = [[0] *10 for _ in range(10)]

    # for y, x in visited:
    #     test_maze[y][x] +=1
    # for i in range(0, 10):
    #     print(test_maze[i])