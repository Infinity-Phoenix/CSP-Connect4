import multiplayer
import ai
import pygame
import pygame_widgets
import button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
PURPLE = (55, 0, 55)
ORANGE = (255, 128, 0)

ROW_COUNT = 12
COLUMN_COUNT = 15
my_font = pygame.font.SysFont("monospace", 75)


def get_mode():
    screen.fill((202, 228, 241))
    # load button images
    ai_img = pygame.image.load("images/button_ai.png").convert_alpha()
    multiplayer_img = pygame.image.load("images/button_multiplayer.png").convert_alpha()

    # create button instances
    ai_button = button.Button(INITIAL_WIDTH / 2 - INITIAL_WIDTH / 4, INITIAL_HEIGHT / 2, ai_img, 1)
    multiplayer_button = button.Button(INITIAL_WIDTH / 2 + INITIAL_WIDTH / 8, INITIAL_HEIGHT / 2, multiplayer_img, 1)

    run = True
    while run:

        if ai_button.draw():
            return "ai"

        if multiplayer_button.draw():
            return "multiplayer"

        events = pygame.event.get()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

    return "QUIT"


def get_players():
    screen.fill((202, 228, 241))

    slider_x = 200
    slider_y = 20
    output_x = int(slider_x / 2)
    output_y = 50

    # load image
    continue_img = pygame.image.load("images/button_continue.png").convert_alpha()

    # create button instance
    continue_button = button.Button(INITIAL_WIDTH / 2 + slider_x / 8, INITIAL_HEIGHT / 2 + 75, continue_img, 1)
    continue_button.draw()

    # create slider/textbox instance
    slider = Slider(screen, int(INITIAL_WIDTH / 2), int(INITIAL_HEIGHT / 2), slider_x, slider_y, min=2, max=6, step=1)
    output = TextBox(screen, int(INITIAL_WIDTH / 2 + slider_x / 4), int(INITIAL_HEIGHT / 2 - 75), output_x, output_y, fontSize=40)

    # create text
    label = my_font.render("Select number of players", 1, BLACK)
    screen.blit(label, (50, 15))

    output.disable()
    run = True
    while run:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        screen.fill((202, 228, 241))

        if continue_button.draw():
            return slider.getValue()

        slider.draw()
        output.setText(slider.getValue())
        pygame_widgets.update(events)
        pygame.display.update()


def get_gamemode():
    screen.fill((202, 228, 241))

    # load image
    line_img = pygame.image.load('images/button_line.png').convert_alpha()
    box_img = pygame.image.load("images/button_box.png").convert_alpha()
    plus_img = pygame.image.load('images/button_plus.png').convert_alpha()


    # create button instance
    line_button = button.Button(INITIAL_WIDTH / 4 - INITIAL_WIDTH / 16, INITIAL_HEIGHT / 2, line_img, 1)
    box_button = button.Button(INITIAL_WIDTH / 2 - INITIAL_WIDTH / 16, INITIAL_HEIGHT / 2, box_img, 1)
    plus_button = button.Button(3 * INITIAL_WIDTH / 4 - INITIAL_WIDTH / 16, INITIAL_HEIGHT / 2, plus_img, 1)

    run = True
    while run:

        if line_button.draw():
            return "line"

        if box_button.draw():
            return "box"

        if plus_button.draw():
            return "plus"

        events = pygame.event.get()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


# menu screen-----------------------------------------------------------------------------------------------------------

pygame.init()
pygame.font.init()  # Initialize the font system
INITIAL_WIDTH = 1000
INITIAL_HEIGHT = INITIAL_WIDTH * (9 / 16)
# create game board-----------------------------------------------------------------------------------------------------
run = True

while run:
    screen = pygame.display.set_mode((INITIAL_WIDTH, INITIAL_HEIGHT))
    screen.fill((202, 228, 241))

    mode = get_mode()
    if mode == "multiplayer":
        players = get_players()
        gamemode = get_gamemode()
        multiplayer.play_game(players, gamemode)

    if mode == "ai":
        ai.play_game()

    screen.fill((202, 228, 241))

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    pygame.quit()
    # remove this to make it loop infinitely, but the slider gfx is glitched out the second time through (because of the
    # module I think)



