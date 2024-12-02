## 창을 띄워 미로를 생성하고 해결
import pygame
import sys
import generator
import time
import threading
import importlib

#버튼 클래스
class Button:
    def __init__(self, surface, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.surface = surface

    def draw(self):
        pygame.draw.rect(self.surface, (200, 200, 200), self.rect)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
        
# 체크박스 클래스
class CheckBox:
    def __init__(self, surface, text, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.checked = False
        self.text = text
        self.text_surface = font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(topleft=(x + size + 5, y))
        self.surface = surface

    def draw(self):
        # 체크박스 배경 그리기
        pygame.draw.rect(self.surface, (200, 200, 200), self.rect)
        # 체크된 경우 체크 표시 그리기
        if self.checked:
            pygame.draw.line(self.surface, (0, 0, 0), (self.rect.x, self.rect.y), (self.rect.x + self.rect.width, self.rect.y + self.rect.height), 3)
            pygame.draw.line(self.surface, (0, 0, 0), (self.rect.x + self.rect.width, self.rect.y), (self.rect.x, self.rect.y + self.rect.height), 3)
        # 텍스트 그리기
        self.surface.blit(self.text_surface, self.text_rect)

    def toggle(self, pos):
        if self.rect.collidepoint(pos):
            self.checked = not self.checked

# make 함수 정의
def make():
    grid[2][2] = 1  # 그리드의 각 칸을 1로 초기화 (예시)

# 그리드 그리기
def draw_grid(n):

    cell_size = (screen_size[0]-100) // n
    #벽은 0 길은 1 방문경로는 2 최종경로는 3
    for i in range(n):
        for j in range(n):
            rect = pygame.Rect(j * cell_size, i * cell_size + 60, cell_size, cell_size)
            if grid[i][j] == 0:
                color = (0, 0, 0)  # 그리드 칸이 벽이라면 검은색
            elif grid[i][j] == 1: #그리드 칸이 길라면 회색
                color = (200, 200, 200)
            elif grid[i][j] == "visited": #그리드 칸이 방문 경로라면 파란색
                color = (0, 0, 255)
            elif grid[i][j] == "path": #그리드 칸이 최종 경로라면 초록색
                color = (0, 255, 0)
            else:
                color = (200, 200, 200)  # 기본 색상
            pygame.draw.rect(screen, color, rect, 0)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)  # 경계선

#Generator 버튼 팝업 함수            
def generator_popup(generator_module):
    popup_active = True
    show_progress = CheckBox(screen, "Show Progress?", screen_size[0] // 2 - 100, screen_size[1] // 2 - 70, 20)
    while popup_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                popup_active = False

        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        text_surface = font.render("Select Solver:", True, (0, 0, 0))
        screen.blit(text_surface, (screen_size[0] // 2 - text_surface.get_width() // 2, screen_size[1] // 2 - 300))

        # 항목 버튼 그리기
        item_buttons = [
            Button(screen, "Recursive_Backtracking", screen_size[0] // 2 - 100, screen_size[1] // 2 - 250, 200, 50),
            Button(screen, "Prim", screen_size[0] // 2 - 100, screen_size[1] // 2 - 190, 200, 50),
            Button(screen, "Eller's Algorithm", screen_size[0] // 2 - 100, screen_size[1] // 2 - 130, 200, 50),
        ]
        for button in item_buttons:
            button.draw()
        # 체크박스 그리기
        show_progress.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button_index in range(len(item_buttons)):
                    if item_buttons[button_index].is_clicked(pos):
                        visited = generator_module[button_index].generator(grid_size)

                        popup_active = False
                show_progress.toggle(pos)
                
    return visited, show_progress.checked

#Solver 버튼 팝업 함수            
def solver_popup(solver_module):
    popup_active = True
    show_progress = CheckBox(screen, "Show Progress?", screen_size[0] // 2 - 100, screen_size[1] // 2 + 170, 20)
    while popup_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                popup_active = False

        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 48)
        text_surface = font.render("Select Solver:", True, (0, 0, 0))
        screen.blit(text_surface, (screen_size[0] // 2 - text_surface.get_width() // 2, screen_size[1] // 2 - 300))

        # 항목 버튼 그리기
        item_buttons = [
            Button(screen, "BFS", screen_size[0] // 2 - 100, screen_size[1] // 2 - 250, 200, 50),
            Button(screen, "DFS", screen_size[0] // 2 - 100, screen_size[1] // 2 - 190, 200, 50),
            Button(screen, "Dijkstra", screen_size[0] // 2 - 100, screen_size[1] // 2 - 130, 200, 50),
            Button(screen, "A-Star", screen_size[0] // 2 - 100, screen_size[1] // 2 - 70, 200, 50),
            Button(screen, "Random Mouse", screen_size[0] // 2 - 100, screen_size[1] // 2 - 10, 200, 50),
            Button(screen, "Right-Hand", screen_size[0] // 2 - 100, screen_size[1] // 2 + 50, 200, 50),
            Button(screen, "Tremaux", screen_size[0] // 2 - 100, screen_size[1] // 2 + 110, 200, 50),
            
        ]

        for button in item_buttons:
            button.draw()
        # 체크박스 그리기
        show_progress.draw()
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button_index in range(len(item_buttons)):
                    if item_buttons[button_index].is_clicked(pos):
                        visited, paths = solver_module[button_index].solver(grid, (0, 0), (grid_size-1, grid_size-1))

                        popup_active = False
                show_progress.toggle(pos)
    return visited, paths, show_progress.checked

#완성된 미로 출력
def draw_maze(visited, show_progress):
    for visit in visited:
        grid[visit[0]][visit[1]] = visit[2]
        if show_progress:
            time.sleep(0.01)
#계산된 경로 출력
def draw_path(visited, paths, show_progress):
    if show_progress:
        for visit in visited:
            grid[visit[0]][visit[1]] = "visited"
            time.sleep(0.01)
    for path in paths:
        grid[path[0]][path[1]] = "path"
#경로 지우기        
def clear_path():
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] == "visited" or grid[x][y] == "path":
                grid[x][y] = 1

#generator 모듈 import
generator_list = ['recursive_backtracking_generator', 'prim_generator', 'ellers_generator']
generator_module = [importlib.import_module(f'generator.{module}') for module in generator_list]
                
#solver 모듈 import
solver_list = ['bfs_solver', 'dfs_solver', 'dijkstra_solver', 'a_star_solver', 'random_mouse_solver', 'righthand_solver', 'tremaux_solver']
solver_module = [importlib.import_module(f'solver.{module}') for module in solver_list]

# Pygame 초기화
pygame.init()

font = pygame.font.Font(None, 36)

# 화면 크기와 색상 설정
screen_size = (900, 900)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('OpenSW_Maze_Project')
button_color = (0, 128, 255)
button_hover_color = (0, 255, 255)
button_rect = pygame.Rect(0, 0, 100, 50)

generate_button = Button(screen, "Generate", 0, 0, 100, 50)
solve_button = Button(screen, "Solve", 110, 0, 100, 50)

# 그리드 설정
grid_size = 21

grid = [[1 for _ in range(grid_size)] for _ in range(grid_size)]

# 메인 루프
running = True
active = False
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
text = ''

#GUI 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if generate_button.is_clicked(event.pos):
                grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)] #경로 생성 전 미리 미로 초기화
                visited, show_progress = generator_popup(generator_module)
                visualizer = threading.Thread(target = draw_maze, args = (visited, show_progress))
                visualizer.start()

            if solve_button.is_clicked(event.pos):
                clear_path() #Solver 실행시 이전에 실행되었던 Solver 흔적 제거
                visited, paths, show_progress = solver_popup(solver_module)
                visualizer = threading.Thread(target = draw_path, args = (visited, paths, show_progress))
                visualizer.start()
                
            if input_box.collidepoint(event.pos):
                active = not active
            color = color_active if active else color_inactive

                
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:

                    grid_size = int(text)
                    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # 화면 업데이트
    screen.fill((255, 255, 255))  # 배경색 흰색
    draw_grid(grid_size)  # 그리드 그리기
    generate_button.draw()
    solve_button.draw()  # 버튼 그리기
    
    # 입력 박스 그리기
    input_box = pygame.Rect(220, 0, 100, 50)
    pygame.draw.rect(screen, (200, 200, 200), input_box, 2)
    text_surface = font.render(text, True, (200, 200, 200))
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
    
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
