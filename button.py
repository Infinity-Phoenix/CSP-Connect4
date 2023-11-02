import pygame

# display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

AI_img = pygame.image.load('images/button_ai.png')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check if mouse is over button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
