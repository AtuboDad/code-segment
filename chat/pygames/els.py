import pygame
import random

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# 定义方块的形状和颜色
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]

# 初始化 pygame
pygame.init()

# 设置窗口大小
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置窗口标题
pygame.display.set_caption("俄罗斯方块")

# 定义字体
font = pygame.font.SysFont(None, 40)

# 定义游戏区域的大小和位置
board_width = 10
board_height = 20
board_x = (screen_width - board_width * 20) // 2
board_y = (screen_height - board_height * 20) // 2

# 定义方块的大小
block_size = 20

# 定义游戏时钟
clock = pygame.time.Clock()

# 定义游戏状态
game_over = False
current_piece = None
next_piece = None
board = [[0] * board_width for _ in range(board_height)]
score = 0

# 定义生成新方块的函数
def new_piece():
    global current_piece, next_piece
    next_piece = random.choice(SHAPES)
    current_piece = next_piece
    return

# 定义绘制游戏区域的函数
def draw_board():
    for y in range(board_height):
        for x in range(board_width):
            if board[y][x]!= 0:
                pygame.draw.rect(screen, GRAY, (board_x + x * block_size, board_y + y * block_size, block_size, block_size))

# 定义绘制当前方块的函数
def draw_piece(piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j]!= 0:
                pygame.draw.rect(screen, piece[i][j], (board_x + (x + j) * block_size, board_y + (y + i) * block_size, block_size, block_size))

# 定义绘制下一个方块的函数
def draw_next_piece(piece):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j]!= 0:
                pygame.draw.rect(screen, piece[i][j], (screen_width - 100 + j * block_size, 50 + i * block_size, block_size, block_size))

# 定义绘制分数的函数
def draw_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

# 定义检查是否可以移动的函数
def is_valid_move(piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j]!= 0:
                if x + j < 0 or x + j >= board_width or y + i >= board_height or board[y + i][x + j]!= 0:
                    return False
    return True

# 定义消除行的函数
def clear_lines():
    global score
    lines_cleared = 0
    for y in range(board_height):
        if 0 not in board[y]:
            del board[y]
            board.insert(0, [0] * board_width)
            lines_cleared += 1
    score += lines_cleared ** 2

# 游戏主循环
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if is_valid_move(current_piece, current_piece_x - 1, current_piece_y):
                    current_piece_x -= 1
            elif event.key == pygame.K_RIGHT:
                if is_valid_move(current_piece, current_piece_x + 1, current_piece_y):
                    current_piece_x += 1
            elif event.key == pygame.K_DOWN:
                if is_valid_move(current_piece, current_piece_x, current_piece_y + 1):
                    current_piece_y += 1
            elif event.key == pygame.K_UP:
                rotated_piece = list(zip(*reversed(current_piece)))
                if is_valid_move(rotated_piece, current_piece_x, current_piece_y):
                    current_piece = rotated_piece

    # 如果当前方块不存在，则生成新的方块
    if current_piece is None:
        new_piece()
        current_piece_x = board_width // 2 - len(current_piece[0]) // 2
        current_piece_y = 0

    # 移动方块
    if is_valid_move(current_piece, current_piece_x, current_piece_y + 1):
        current_piece_y += 1
    else:
        # 如果不能移动，则将当前方块放置在游戏区域中
        for i in range(len(current_piece)):
            for j in range(len(current_piece[i])):
                if current_piece[i][j]!= 0:
                    board[current_piece_y + i][current_piece_x + j] = current_piece[i][j]
        clear_lines()
        current_piece = None

    # 绘制游戏界面
    screen.fill(BLACK)
    draw_board()
    if current_piece is not None:
        draw_piece(current_piece, current_piece_x, current_piece_y)
    draw_next_piece(next_piece)
    draw_score()
    pygame.display.update()

    # 设置游戏帧率
    clock.tick(10)

# 退出游戏
pygame.quit()
