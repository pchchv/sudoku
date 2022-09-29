import pygame


BLACK = (0, 0, 0)
pygame.init()
X = 300
Y = 200
size = (X, Y)
window = pygame.display.set_mode(size)


def buttonDrawer(left, top, color, textInButton):
    rectSize = pygame.Rect(left, top, 60, 30)
    pygame.draw.rect(window, color, rectSize)  # left, top, width, height
    pygame.draw.rect(window, BLACK, rectSize, 3)
    fontButton = pygame.font.Font('freesansbold.ttf', 20)
    textButton = fontButton.render(textInButton, True, BLACK, )
    textRectButton = textButton.get_rect()
    textRectButton.center = (left + 30, top + 15)
    window.blit(textButton, textRectButton)
