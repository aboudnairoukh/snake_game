from game_display import GameDisplay
from game import Game

UP = 'Up'
DOWN = 'Down'
LEFT = 'Left'
RIGHT = 'Right'

BLACK = 'black'
GREEN = 'green'
RED = 'red'
ORANGE = 'orange'

DEAD = 0
ALIVE = 1


def key_interpreter(previous_key, new_key):
    """This function checks the validity of the direction input, and updates
    the direction as needed, if no direction is entered, the last direction is
    returned"""
    if (previous_key in (RIGHT, LEFT) and new_key in (UP, DOWN)) \
            or (
            previous_key in (UP, DOWN) and new_key in (RIGHT, LEFT)):
        return new_key
    else:
        return previous_key


def draw_snake(gd, game):
    """This function draws the snake on the board"""
    for cord in game.get_snake().get_cords():
        if game.in_bound(cord) and cord != game.get_bomb().get_coordinate() \
                and cord not in game.get_bomb().get_explosion_coordinates():
            gd.draw_cell(cord[0], cord[1], BLACK)


def draw_apples(gd, game):
    """This function draws the apples on the board"""
    for apple in game.get_apples_lst():
        cord = apple.get_coordinate()
        gd.draw_cell(cord[0], cord[1], GREEN)


def draw_bomb(gd, game):
    """This function draws the bomb on the board"""
    coordinate = game.get_bomb().get_coordinate()
    gd.draw_cell(coordinate[0], coordinate[1], RED)


def draw_explosion(gd, game):
    """This function draws the explosion on the board"""
    for cord in game.get_bomb().get_explosion_coordinates():
        if game.in_bound(cord):
            gd.draw_cell(cord[0], cord[1], ORANGE)


def draw_board(gd, game):
    """This function draws the objects on the board every round"""
    draw_apples(gd, game)
    draw_snake(gd, game)
    if game.get_bomb().exploded():
        draw_explosion(gd, game)
    else:
        draw_bomb(gd, game)


def main_loop(gd: GameDisplay) -> None:
    """This function runs the game"""
    game = Game()
    draw_snake(gd, game)
    draw_bomb(gd, game)
    draw_apples(gd, game)
    key_clicked = UP
    gd.show_score(game.get_score())
    gd.end_round()
    while True:
        key_clicked = key_interpreter(key_clicked, gd.get_key_clicked())
        game.snake_move_forward(key_clicked)
        is_snake_dead = game.is_dead()
        game.did_eat_an_apple()
        if not is_snake_dead:
            is_snake_dead = game.bomb_situation()
            game.completing_apples()
        if is_snake_dead:
            draw_board(gd, game)
            gd.end_round()
            break
        draw_board(gd, game)
        gd.show_score(game.get_score())
        gd.end_round()
