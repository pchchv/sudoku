import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
L_GREEN = (150, 255, 150)
RED = (255, 0, 0)
L_RED = (255, 204, 203)
GRAY = (60, 60, 60)
L_GRAY = (220, 220, 220)
YELLOW = (255, 255, 0)
WIDTH = HEIGHT = 50
MARGIN = 5
pygame.init()
X = 300
Y = 200
size = (X, Y)
window = pygame.display.set_mode(size)
font = pygame.font.Font('freesansbold.ttf', 25)


def button_drawer(left, top, color, textInButton):
    rect_size = pygame.Rect(left, top, 60, 30)
    pygame.draw.rect(window, color, rect_size)  # left, top, width, height
    pygame.draw.rect(window, BLACK, rect_size, 3)
    font_button = pygame.font.Font('freesansbold.ttf', 20)
    text_button = font_button.render(textInButton, True, BLACK, )
    text_rect_button = text_button.get_rect()
    text_rect_button.center = (left + 30, top + 15)
    window.blit(text_button, text_rect_button)


def level_selector():
    level = 0
    text = font.render('choose difficulty level', True, BLACK, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (X // 2, Y // 2 - 40)
    pygame.display.set_caption("Sudoku King")
    done = True
    while done:
        window.fill(WHITE)
        window.blit(text, text_rect)
        button_drawer(40, 100, GRAY, "1")
        button_drawer(120, 100, GRAY, "2")
        button_drawer(200, 100, GRAY, "3")
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Deactivates the pygame library
                pygame.quit()
                # Quit the program
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("Click ", pos)
                if (40 <= pos[0] <= 100) and (100 <= pos[1] <= 130):
                    level = 1
                if (120 <= pos[0] <= 180) and (100 <= pos[1] <= 130):
                    level = 2
                if (200 <= pos[0] <= 260) and (100 <= pos[1] <= 130):
                    level = 3
                if level != 0:
                    # print(level)
                    pygame.quit()
                    return level
            # Draws the surface object to the screen
            pygame.display.update()
