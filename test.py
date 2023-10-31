import numpy as np
import pygame
import sys
import math


# colors in rgb value
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
PURPLE = (55, 0, 55)
ORANGE = (255, 128, 0)

# constants for menu
players = 6
ROW_COUNT = 12
COLUMN_COUNT = 15


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

# Code created by Arya Kunisetty
# Checks if player has won the game
def winning_move(board, piece):
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

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True

# Draws the Board
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 3:
                pygame.draw.circle(screen, GREEN, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 4:
                pygame.draw.circle(screen, PINK, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 5:
                pygame.draw.circle(screen, ORANGE, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 6:
                pygame.draw.circle(screen, PURPLE, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()
    # Code created by ak47

board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 50

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            elif turn==1:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
            elif turn==2:
                pygame.draw.circle(screen,GREEN, (posx, int(SQUARESIZE / 2)), RADIUS)
            elif turn==3:
                pygame.draw.circle(screen, PINK, (posx, int(SQUARESIZE / 2)), RADIUS)
            elif turn==4:
                pygame.draw.circle(screen, ORANGE, (posx, int(SQUARESIZE / 2)), RADIUS)
            elif turn==5:
                pygame.draw.circle(screen, PURPLE, (posx, int(SQUARESIZE / 2)), RADIUS)

        # Actual game play with inputs
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (50, -15))
                        game_over = True


            # # Ask for Player 2 Input
            if(turn==1):
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (50, -15))
                        game_over = True

            # Code created by ak47

            # # Ask for Player 3 Input
            if(turn==2):
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):

                    row = get_next_open_row(board, col)

                    drop_piece(board, row, col, 3)

                    if winning_move(board, 3):
                        label = myfont.render("Player 3 wins!!", 1, GREEN)

                        screen.blit(label, (50, -15))

                        game_over = True
            if (turn == 3):
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 4)

                    if winning_move(board, 4):
                        label = myfont.render("Player 4 wins!!", 1, PINK)
                        screen.blit(label, (50, -15))
                        game_over = True

            if (turn == 4):
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):

                    row = get_next_open_row(board, col)

                    drop_piece(board, row, col, 5)

                    if winning_move(board, 5):
                        label = myfont.render("Player 5 wins!!", 1, ORANGE)

                        screen.blit(label, (50, -15))

                        game_over = True

            if (turn == 5):
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):

                    row = get_next_open_row(board, col)

                    drop_piece(board, row, col, 6)

                    if winning_move(board, 6):
                        label = myfont.render("Player 6 wins!!", 1, PURPLE)

                        screen.blit(label, (50, -15))

                        game_over = True


            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % players


        if game_over:
             pygame.time.delay(10000)

# Code created by ak47
