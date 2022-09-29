from solver import *
from level import *
import pygame
import time


numbers_1to9 = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]


def border_drawer():
    dif = 500 // 9
    for i in range(10):
        thick = 5
        pygame.draw.line(screen, GRAY, (0, i * dif + 2), (500, i * dif + 2), thick)
        pygame.draw.line(screen, GRAY, (i * dif + 2, 0), (i * dif + 2, 500), thick)
    for i in range(10):
        if i % 3 == 0:
            thick = 8
            pygame.draw.line(screen, BLACK, (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, BLACK, (i * dif, 0), (i * dif, 500), thick)


def init_board_drawer():
    for ROW in range(len(Board)):
        for COLUMN in range(len(Board[ROW])):
            color = L_GRAY
            if Board[row][COLUMN] == 0:  # if we want to change to background of the empty cells
                color = WHITE
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * COLUMN + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            # Show nothing if the number is 0
            font = pygame.font.Font('freesansbold.ttf', 32)
            if Board[row][COLUMN] == 0:
                text = font.render(" ", True, BLACK, )  # render(text, anti-alias[True], color, background=None)
            else:
                text = font.render(str(Board[row][COLUMN]), True, BLACK, )

            text_rect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface
            text_rect.center = (
                (MARGIN + WIDTH) * COLUMN + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
            screen.blit(text, text_rect)
            border_drawer()


def cheating_all_the_way(solved_board):
    for ROW in range(len(Board)):
        for COLUMN in range(len(Board[ROW])):
            Board[ROW][COLUMN] = solved_board[ROW][COLUMN]
            add_num_to_board(Board[ROW][COLUMN], ROW, COLUMN, L_GREEN)
            time.sleep(0.05)
            pygame.display.flip()
    finish()


def add_num_to_board(number, ROW, COLUMN, color):
    add_new_rect(ROW, COLUMN, WHITE, 5)
    add_new_rect(ROW, COLUMN, color, None)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(number), True, BLACK, )
    text_rect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface
    text_rect.center = ((MARGIN + WIDTH) * COLUMN + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * ROW + MARGIN + WIDTH / 2)
    screen.blit(text, text_rect)
    border_drawer()


def add_new_rect(row, col, color, width):
    rect_size = pygame.Rect((MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT)
    if width is not None:
        pygame.draw.rect(screen, color, rect_size, width)  # Coloring only the border
    else:
        pygame.draw.rect(screen, color, rect_size)  # Coloring the whole rectangle


def flickering(time_flickering, color):  # Flickering with color on-off
    add_new_rect(row, column, color, 5)
    pygame.display.flip()
    time.sleep(time_flickering)
    add_new_rect(row, column, WHITE, 5)
    pygame.display.flip()
    time.sleep(time_flickering)
    add_new_rect(row, column, color, 5)
    pygame.display.flip()
    time.sleep(time_flickering)
    add_new_rect(row, column, WHITE, 5)
    pygame.display.flip()


def finish(solved_board):
    if solved_board == Board:
        print("good")
    else:
        print("not good")


if __name__ == "__main__":
    flag1 = True
    while flag1:
        level = level_selector()
        if level == 1 or level == 2 or level == 3:
            print(level)
            flag1 = False
    pygame.display.set_caption("Sudoku King1")
    screen = pygame.display.set_mode(size)
    sol = main_solver(level)  # First at all the script solve the sudoku by itself
    print("solveBoard")
    board_printer(sol)
    pygame.init()
    screen.fill(BLACK)
    init_board_drawer()
    readyForInput = False
    key = None
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key in numbers_1to9:
                    key = chr(event.key)
                if event.key == pygame.K_RETURN:
                    finish()
                if event.key == pygame.K_c:
                    cheating_all_the_way()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if readyForInput is True:
                    add_new_rect(row, column, WHITE, None)
                    border_drawer()
                    readyForInput = False
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (WIDTH + MARGIN)
                if Board[row][column] == 0:
                    add_new_rect(row, column, YELLOW, 5)
                    readyForInput = True
        if readyForInput and key is not None:
            if int(key) == sol[row][column]:
                Board[row][column] = key
                flickering(0.1, GREEN)  # Flickering at a 0.2 seconds with the color green
                add_num_to_board(key, row, column, L_GREEN)
            else:
                flickering(0.1, RED)  # Flickering at a 0.2 seconds with the color red
                add_num_to_board(key, row, column, L_RED)
            border_drawer()
            readyForInput = False
        key = None
        pygame.display.flip()
        pygame.display.update()


# Close the window and quit
pygame.quit()