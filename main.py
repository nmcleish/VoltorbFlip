# Simple pygame program

# Import and initialize the pygame library
import pygame
import os
import voltorbflip

pygame.init()

display_width = 600
display_height = 600

pygame.display.set_caption('Voltorb Flip')

# Set up the drawing window
screen = pygame.display.set_mode([display_width, display_height])

# Insert images
square_size = 50
square_img = pygame.image.load(os.path.join('img_square.jpg'))
square_img = pygame.transform.scale(square_img, (square_size, square_size))

# Insert images
voltorb_size = 50
voltorb_img = pygame.image.load(os.path.join('voltorb.png'))
voltorb_img = pygame.transform.scale(voltorb_img, (voltorb_size, voltorb_size))

# # defining a font
# smallfont = pygame.font.SysFont('Corbel', 35)
#
# # rendering a text written in
# # this font
# text = smallfont.render('quit', True, color)

title_text = pygame.font.Font('freesansbold.ttf', 40)
button_font = pygame.font.Font('freesansbold.ttf', 20)
nav_font = pygame.font.Font('freesansbold.ttf', 15)
game_font = pygame.font.Font('freesansbold.ttf', 13)
space_font = pygame.font.Font('freesansbold.ttf', 15)

background_color = (255, 238, 187)
button_color = (255, 220, 184)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


def draw_square(x, y):
    screen.blit(square_img, (x, y))


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def update_level(level):
    pygame.draw.rect(screen, background_color,
                     pygame.Rect(200, 80, 90, 15))
    TextSurf, TextRect = text_objects(str(level), nav_font, black)
    screen.blit(TextSurf, (200, 80))


def update_coins(coins):
    pygame.draw.rect(screen, background_color,
                     pygame.Rect(200, 60, 90, 15))
    TextSurf, TextRect = text_objects(str(coins), nav_font, black)
    screen.blit(TextSurf, (200, 60))


def update_total_coins(total_coins):
    pygame.draw.rect(screen, background_color,
                     pygame.Rect(200, 40, 90, 15))
    TextSurf, TextRect = text_objects(str(total_coins), nav_font, black)
    screen.blit(TextSurf, (200, 40))


def update_status(status):
    pygame.draw.rect(screen, background_color,
                     pygame.Rect(450, 100, 120, 15))
    TextSurf, TextRect = text_objects(status, nav_font, black)
    screen.blit(TextSurf, (450, 100))


# TODO: Add game instructions
# This is the main menu for the game
def game_intro():
    intro = True
    screen.fill(background_color)

    # Title on main menu screen
    TextSurf, TextRect = text_objects("Voltorb Flip", title_text, black)
    TextRect.center = ((display_width / 2), (display_height / 9))
    screen.blit(TextSurf, TextRect)

    # Start Button
    pygame.draw.rect(screen, button_color, pygame.Rect(display_width / 2 - 75, display_height / 3, 150, 50))
    TextSurf, TextRect = text_objects("Start", button_font, black)
    TextRect.center = ((display_width / 2), (display_height / 3 + 25))
    screen.blit(TextSurf, TextRect)

    # Instructions Button
    pygame.draw.rect(screen, button_color, pygame.Rect(display_width / 2 - 75, display_height / 3 + 100, 150, 50))
    TextSurf, TextRect = text_objects("How to Play", button_font, black)
    TextRect.center = ((display_width / 2), (display_height / 3 + 100 + 25))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    button = ""

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Play Button Click
                if display_width / 2 - 75 <= mouse[0] <= display_width / 2 - 75 + 150 and display_height / 3 <= mouse[1] <= display_height / 3 + 50:
                    intro = False
                    button = "Play"

                # Instructions button click
                if display_width / 2 - 75 <= mouse[0] <= display_width / 2 - 75 + 150 and display_height / 3 + 100 <= mouse[1] <= display_height / 3 + 50 + 100:
                    intro = True

        mouse = pygame.mouse.get_pos()

        # Play Button Hover
        if display_width / 2 - 75 <= mouse[0] <= display_width / 2 - 75 + 150 and display_height / 3 <= mouse[1] <= display_height / 3 + 50:
            pygame.draw.rect(screen, black, pygame.Rect(display_width / 2 - 75, display_height / 3, 150, 50), 3)
        else:
            pygame.draw.rect(screen, button_color, pygame.Rect(display_width / 2 - 75, display_height / 3, 150, 50), 3)

        # Instructions Button Hover
        if display_width / 2 - 75 <= mouse[0] <= display_width / 2 - 75 + 150 and display_height / 3 + 100 <= mouse[
            1] <= display_height / 3 + 50 + 100:
            pygame.draw.rect(screen, black, pygame.Rect(display_width / 2 - 75, display_height / 3 + 100, 150, 50), 3)
        else:
            pygame.draw.rect(screen, button_color, pygame.Rect(display_width / 2 - 75, display_height / 3 + 100, 150, 50), 3)

        pygame.display.update()

    if button == "Play":
        run_game()
    elif button == "Instructions":
        None

# Draws the game board
def draw_game_board(game):
    voltorb_row = game.board.get_row_voltorbs()
    point_row = game.board.get_row_points()

    voltorb_col = game.board.get_col_voltorbs()
    point_col = game.board.get_col_points()

    board_spaces = {}

    for x in range(0, 6):
        for y in range(0, 6):
            square_x = display_width / 9 + display_width / 9 * y - 20
            square_y = display_height / 9 + display_height / 9 * x + 50

            if x == 5 and y == 5:
                break
            elif x == 5 or y == 5:
                pygame.draw.rect(screen, white,
                                 pygame.Rect(square_x, square_y, square_size, square_size))

                x_mid = square_x + square_size / 2
                if y == 5:
                    TextSurf, TextRect = text_objects(str(point_row[x]), game_font, black)
                    TextRect.center = (x_mid, square_y + square_size / 4)
                    screen.blit(TextSurf, TextRect)

                    pygame.draw.line(screen, black, (x_mid - 6, square_y + square_size / 2),
                                     (x_mid + 6, square_y + square_size / 2))

                    TextSurf, TextRect = text_objects(str(voltorb_row[x]), game_font, red)
                    TextRect.center = (x_mid, square_y + square_size / 4 * 3)
                    screen.blit(TextSurf, TextRect)
                    print("one step")

                if x == 5:
                    TextSurf, TextRect = text_objects(str(point_col[y]), game_font, black)
                    TextRect.center = (x_mid, square_y + square_size / 4)
                    screen.blit(TextSurf, TextRect)

                    pygame.draw.line(screen, black, (x_mid - 6, square_y + square_size / 2),
                                     (x_mid + 6, square_y + square_size / 2))

                    TextSurf, TextRect = text_objects(str(voltorb_col[y]), game_font, red)
                    TextRect.center = (x_mid, square_y + square_size / 4 * 3)
                    screen.blit(TextSurf, TextRect)

            else:
                board_spaces[(square_x, square_y)] = (x, y)
                draw_square(square_x, square_y)
    pygame.display.update()
    return board_spaces


# TODO: Add quit button
def run_game():

    # Fill the background
    screen.fill(background_color)

    game = voltorbflip.Game()

    board_spaces = draw_game_board(game)

    # Return to Menu Button
    TextSurf, TextRect = text_objects("Return to Menu", nav_font, black)
    screen.blit(TextSurf, (60, 20))

    # Show Total Coins
    TextSurf, TextRect = text_objects("Total Coins:", nav_font, black)
    screen.blit(TextSurf, (60, 40))

    # Show Coins
    TextSurf, TextRect = text_objects("Coins:", nav_font, black)
    screen.blit(TextSurf, (60, 60))

    # Show level
    TextSurf, TextRect = text_objects("Level:", nav_font, black)
    screen.blit(TextSurf, (60, 80))

    # Show Total Coins
    update_total_coins(0)

    # Show Coins
    update_coins(0)

    # Show level
    update_level(1)

    # Run until the user asks to quit
    running = True
    level_complete = False
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                running = False

            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not level_complete:
                    for square in board_spaces.keys():
                        if square[0] <= mouse[0] <= square[0] + square_size and square[1] <= mouse[1] <= square[1] + square_size:
                            result = game.check_space(board_spaces[square])
                            print(board_spaces[square])
                            del board_spaces[square]
                            print(result)

                            # update coins
                            update_coins(result[1])

                            pygame.draw.rect(screen, white,
                                             pygame.Rect(square[0], square[1], square_size, square_size))
                            pygame.draw.rect(screen, white,
                                             pygame.Rect(square[0] - 2, square[1] - 2, square_size + 4, square_size + 4), 1)
                            if result[0]:
                                TextSurf, TextRect = text_objects(str(result[0]), space_font, black)
                                TextRect.center = (square[0] + square_size / 2, square[1] + square_size / 2)
                                screen.blit(TextSurf, TextRect)
                            else:
                                screen.blit(voltorb_img, square)

                            if result[3] != "":
                                level_complete = True
                                update_total_coins(result[2])

                                # Game Status
                                update_status(result[3])


                                # New Game Button
                                pygame.draw.rect(screen, button_color, pygame.Rect(450, 150, 100, 50))
                                TextSurf, TextRect = text_objects("New Game", nav_font, black)
                                TextRect.center = (450 + 50, 150 + 25)
                                screen.blit(TextSurf, TextRect)

                                for board_space in board_spaces.keys():
                                    pygame.draw.rect(screen, white,
                                                     pygame.Rect(board_space[0], board_space[1], square_size, square_size))

                                    result = game.get_space(board_spaces[board_space])
                                    if result:
                                        TextSurf, TextRect = text_objects(str(result), space_font, black)
                                        TextRect.center = (board_space[0] + square_size / 2, board_space[1] + square_size / 2)
                                        screen.blit(TextSurf, TextRect)
                                    else:
                                        screen.blit(voltorb_img, board_space)
                            break
                else:
                    if 450 <= mouse[0] <= 450 + 100 and 150 <= mouse[1] <= 150 + 40:
                        pygame.draw.rect(screen, background_color, pygame.Rect(450, 150, 100, 50), 2)
                        game.new_board()
                        board_spaces = draw_game_board(game)
                        level_complete = False

                        # Erase Coins
                        update_coins(0)
                        update_level(game.get_level())
                        update_status("")

                        pygame.draw.rect(screen, background_color, pygame.Rect(450, 150, 100, 50))


                            # draw whole board
        mouse = pygame.mouse.get_pos()

        # Highlight space on hover
        if not level_complete:
            for square in board_spaces.keys():
                if square[0] <= mouse[0] <= square[0] + square_size and square[1] <= mouse[1] <= square[1] + square_size:
                    pygame.draw.rect(screen, black, pygame.Rect(square[0] - 2, square[1] - 2, square_size + 4, square_size + 4), 1)
                else:
                    pygame.draw.rect(screen, white, pygame.Rect(square[0] - 2, square[1] - 2, square_size + 4, square_size + 4), 1)
        else:
            if 450 <= mouse[0] <= 450 + 100 and 150 <= mouse[1] <= 150 + 40:
                pygame.draw.rect(screen, black, pygame.Rect(450, 150, 100, 50), 2)
            else:
                pygame.draw.rect(screen, background_color, pygame.Rect(450, 150, 100, 50), 2)


        pygame.display.update()


game_intro()
# Done! Time to quit.
pygame.quit()
quit()
