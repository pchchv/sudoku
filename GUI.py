import pygame
from solver import *
from level import *


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


def finish():
    if solvedBoard == Board:
        print("good")
    else:
        print("not good")
