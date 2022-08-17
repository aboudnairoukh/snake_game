from game_parameters import *
from snake import *
from apple import *
from bomb import *


class Game:
    """This class represent a singe game"""

    def __init__(self):
        self.__snake = Snake()
        snake_coordinates = self.__snake.get_cords()
        self.__apples_lst = []
        self.__bomb = None
        self.__bomb = self.__generate_bomb()
        for i in range(3):
            apple = self.__generate_apple(snake_coordinates)
            self.__apples_lst.append(apple)
        self.__score = 0

    def in_bound(self, coordinate):
        """This function returns True if the given coordinate is in the
        board's limits and False if not"""
        return (0 <= coordinate[1] <= game_parameters.HEIGHT - 1 and
                0 <= coordinate[0] <= game_parameters.WIDTH - 1)

    def __empty_coordinate(self, coordinate, snake_cords):
        """This function returns True if the given coordinate is empty and
        False if not"""
        if coordinate in snake_cords:
            return False
        if self.__bomb is not None and \
                coordinate == self.__bomb.get_coordinate():
            return False
        for apple in self.__apples_lst:
            if coordinate == apple.get_coordinate():
                return False
        return True

    def __generate_bomb(self):
        """This function generates and returns a bomb in an empty coordinate"""
        x, y, radius, time = get_random_bomb_data()
        while not self.__empty_coordinate((x, y), self.__snake.get_cords()):
            x, y, radius, time = get_random_bomb_data()
        return Bomb((x, y), radius, time)

    def num_of_empty_cells(self):
        """This function returns the number of current empty cells in the
        board"""
        return (HEIGHT * WIDTH - self.__snake.get_length() - 1 -
                len(self.__apples_lst))

    def __generate_apple(self, snake_cords):
        """This function generates and returns a singe apple"""
        x, y, score = get_random_apple_data()
        while not self.__empty_coordinate((x, y), snake_cords):
            x, y, score = get_random_apple_data()
        return Apple((x, y), score)

    def get_snake(self):
        """This function returns the snake of the current game"""
        return self.__snake

    def get_apples_lst(self):
        """This function returns the list of the current valid apples in the
        game"""
        return self.__apples_lst

    def get_bomb(self):
        """This function returns the bomb of the current game"""
        return self.__bomb

    def get_score(self):
        """This function returns the current score in the current game"""
        return self.__score

    def snake_move_forward(self, key_clicked):  # needed?
        """This function moves the game's snake a step in the given
        direction"""
        self.__snake.move_forward(key_clicked)

    def is_dead(self):
        """This function checks if the snake collides with itself ,a bomb,
        with an explosion or if it is not in bound"""
        if not self.in_bound(self.__snake.get_head_value()):
            return True
        if self.__bomb.get_coordinate() == self.__snake.get_head_value():
            return True
        if self.__snake.get_head_value() in \
                self.__bomb.get_explosion_coordinates():
            return True
        if (len(set(self.__snake.get_cords())) != self.__snake.get_length() and
                self.get_snake().get_head_value() !=
                self.get_snake().get_tail_value()):
            return True
        return False

    def did_eat_an_apple(self):
        """This function checks if the snake ate an apple or not, if yes it
        updates the score, and thr function extend the snake as much as
        needed"""
        if self.__snake.get_more_to_extend() == 0:
            self.__snake.remove_tail()
        else:
            self.__snake.extended()
        for apple in self.__apples_lst:
            if self.__snake.get_head_value() == apple.get_coordinate():
                self.__snake.ate_an_apple()
                self.__score += apple.get_score()
                self.__apples_lst.remove(apple)

    def bomb_situation(self):
        """This function checks if the bomb exploded or not, if the snake
        collides with the explosion, if the bomb exploded and the
        explosion didn't end it updates the radius, if the bomb didn't it
        updates the timer, and if needed the function generates a new bomb"""
        if not self.__bomb.exploded():
            self.__bomb.update_time()
        elif self.__bomb.exploded() and self.__bomb.get_radius() != 0:
            self.__bomb.update_radius()
            explosion_coordinates = self.__bomb.get_explosion_coordinates()
            for thrust in explosion_coordinates:
                if thrust in self.__snake.get_cords():
                    return True
            for apple in self.__apples_lst:
                if apple.get_coordinate() in explosion_coordinates:
                    self.__apples_lst.remove(apple)
        elif self.__bomb.exploded() and self.__bomb.get_radius() == 0:
            self.__bomb = self.__generate_bomb()
        return False

    def won(self):
        """This function checks if the board is full or not"""
        if self.__snake.get_length() == \
                game_parameters.WIDTH * game_parameters.HEIGHT - 3:
            return True
        return False

    def completing_apples(self):
        """This function completes the apples on the board"""
        while len(self.__apples_lst) < 3 and self.num_of_empty_cells() != 0:
            self.__apples_lst.append(
                self.__generate_apple(self.__snake.get_cords()))
