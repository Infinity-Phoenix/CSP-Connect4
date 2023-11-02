import math
import sys
import numpy as np
import pygame

pygame.init()

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
PURPLE = (55, 0, 55)
ORANGE = (255, 128, 0)

colors = [RED, YELLOW, GREEN, PINK, ORANGE, PURPLE]

ROW_COUNT = 12
COLUMN_COUNT = 15

SQUARE_SIZE = 50
width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)
RADIUS = int(SQUARE_SIZE / 2 - 5)
my_font = pygame.font.SysFont("monospace", 75)


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece, gamemode):

    if gamemode == "line":
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][
                            c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][
                            c + 3] == piece:
                    return True

    if gamemode == "plus":
        for c in range(COLUMN_COUNT - 2):
            for r in range(ROW_COUNT - 2):
                if board[r + 1][c] == piece and board[r][c + 1] == piece and board[r + 1][c + 1] == piece and \
                        board[r + 2][c + 1] and board[r + 1][c + 2] == piece:
                    return True

    if gamemode == "box":
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT - 1):
            for r in range(ROW_COUNT - 1):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r + 1][c + 1] == piece and board[r + 1][
                    c] == piece:
                    return True


def draw_board(board, screen):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 3:
                pygame.draw.circle(screen, GREEN, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 4:
                pygame.draw.circle(screen, PINK, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 5:
                pygame.draw.circle(screen, ORANGE, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 6:
                pygame.draw.circle(screen, PURPLE, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    pygame.display.update()


def play_game(players, gamemode):
    board = create_board()
    print_board(board)
    pygame.init()
    screen = pygame.display.set_mode(size)
    draw_board(board, screen)
    pygame.display.update()

    turn = 0
    game_over = False
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("ok")
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                pos_x = event.pos[0]
                pygame.draw.circle(screen, colors[turn], (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
                ''''
                if turn == 0:
                    pygame.draw.circle(screen, RED, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
                elif turn == 1:
                    pygame.draw.circle(screen, YELLOW, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
                elif turn == 2:
                    pygame.draw.circle(screen, GREEN, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
                elif turn == 3:
                    pygame.draw.circle(screen, PINK, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
                elif turn == 4:
                    pygame.draw.circle(screen, ORANGE, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
                elif turn == 5:
                    pygame.draw.circle(screen, PURPLE, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
                '''''

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / SQUARE_SIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, turn + 1)

                    if winning_move(board, turn + 1, gamemode):
                        label = my_font.render(f"Player {turn + 1} wins!!", 1, colors[turn])
                        screen.blit(label, (50, -15))
                        game_over = True

                print_board(board)
                draw_board(board, screen)

                turn += 1
                turn = turn % players
            pygame.display.update()
            ''''
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    pos_x = event.pos[0]
                    col = int(math.floor(pos_x / SQUARE_SIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = my_font.render("Player 1 wins!!", 1, RED)
                            screen.blit(label, (50, -15))
                            game_over = True
                
                # # Ask for Player 2 Input
                if turn == 1:
                    pos_x = event.pos[0]
                    col = int(math.floor(pos_x / SQUARE_SIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = my_font.render("Player 2 wins!!", 1, YELLOW)
                            screen.blit(label, (50, -15))
                            game_over = True

                # # Ask for Player 3 Input
                if turn == 2:
                    pos_x = event.pos[0]
                    col = int(math.floor(pos_x / SQUARE_SIZE))

                    if is_valid_location(board, col):

                        row = get_next_open_row(board, col)

                        drop_piece(board, row, col, 3)

                        if winning_move(board, 3):
                            label = my_font.render("Player 3 wins!!", 1, GREEN)

                            screen.blit(label, (50, -15))

                            game_over = True
                if turn == 3:
                    pos_x = event.pos[0]
                    col = int(math.floor(pos_x / SQUARE_SIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 4)

                        if winning_move(board, 4):
                            label = my_font.render("Player 4 wins!!", 1, PINK)
                            screen.blit(label, (50, -15))
                            game_over = True

                if turn == 4:
                    pos_x = event.pos[0]
                    col = int(math.floor(pos_x / SQUARE_SIZE))

                    if is_valid_location(board, col):

                        row = get_next_open_row(board, col)

                        drop_piece(board, row, col, 5)

                        if winning_move(board, 5):
                            label = my_font.render("Player 5 wins!!", 1, ORANGE)

                            screen.blit(label, (50, -15))

                            game_over = True

                if turn == 5:
                    pos_x = event.pos[0]
                    col = int(math.floor(pos_x / SQUARE_SIZE))

                    if is_valid_location(board, col):

                        row = get_next_open_row(board, col)

                        drop_piece(board, row, col, 6)

                        if winning_move(board, 6):
                            label = my_font.render("Player 6 wins!!", 1, PURPLE)

                            screen.blit(label, (50, -15))

                            game_over = True

                print_board(board)
                draw_board(board, screen)

                turn += 1
                turn = turn % players
            '''''

        if game_over:
            pygame.time.delay(1500)
            break
