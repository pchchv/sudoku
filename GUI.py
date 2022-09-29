from solver import *
from level import *
import pygame
import time


screen = pygame.display.set_mode(size)
numbers_1to9 = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]


def borderDrawer():
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


def initBoardDrawer():
    for row in range(len(Board)):
        for column in range(len(Board[row])):
            color = L_GRAY
            if Board[row][column] == 0:  # if we want to change to background of the empty cells
                color = WHITE
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            # Show nothing if the number is 0
            font = pygame.font.Font('freesansbold.ttf', 32)
            if Board[row][column] == 0:
                text = font.render(" ", True, BLACK, )  # render(text, anti-alias[True], color, background=None)
            else:
                text = font.render(str(Board[row][column]), True, BLACK, )

            textRect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface
            textRect.center = (
                (MARGIN + WIDTH) * column + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
            screen.blit(text, textRect)
            borderDrawer()


def cheatingAllTheWay():
    for row in range(len(Board)):
        for column in range(len(Board[row])):
            Board[row][column] = solvedBoard[row][column]
            addNumToBoard(Board[row][column], row, column, L_GREEN)
            time.sleep(0.05)
            pygame.display.flip()
    finish()


def addNumToBoard(number, row, column, color):
    addNewRect(row, column, WHITE, 5)
    addNewRect(row, column, color, None)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(number), True, BLACK, )
    textRect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface
    textRect.center = ((MARGIN + WIDTH) * column + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
    screen.blit(text, textRect)
    borderDrawer()


def addNewRect(row, col, color, width):
    rectSize = pygame.Rect((MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT)
    if width is not None:
        pygame.draw.rect(screen, color, rectSize, width)  # Coloring only the border
    else:
        pygame.draw.rect(screen, color, rectSize)  # Coloring the whole rectangle


def finish():
    if solvedBoard == Board:
        print("good")
    else:
        print("not good")


if __name__ == "__main__":
    flag1 = True
    while flag1:
        level = levelSelector()
        if level == 1 or level == 2 or level == 3:
            print(level)
            flag1 = False
    pygame.display.set_caption("Sudoku King1")
    screen = pygame.display.set_mode(size)
    sol = mainSolver(level)  # Аirst at all the script solve the sudoku by itself
    print("solveBoard")
    boardPrinter(sol)
    pygame.init()
    screen.fill(BLACK)
    initBoardDrawer()
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
                    cheatingAllTheWay()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if readyForInput is True:
                    addNewRect(row, column, WHITE, None)
                    borderDrawer()
                    readyForInput = False
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (WIDTH + MARGIN)
                if Board[row][column] == 0:
                    addNewRect(row, column, YELLOW, 5)
                    readyForInput = True
        key = None
        pygame.display.flip()
        pygame.display.update()


# Close the window and quit
pygame.quit()