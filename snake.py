import game_parameters

DIRECTIONS = {'Up': (0, 1), 'Down': (0, -1), 'Right': (1, 0), 'Left': (-1, 0)}


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def set_next(self, value):
        self.next = Node(value)
        return self.next

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value


class Snake:
    """This class represent the snake (a linked list) of the game"""
    def __init__(self):
        self.__head = Node((game_parameters.WIDTH // 2,
                            game_parameters.HEIGHT // 2))
        self.__tail = Node((game_parameters.WIDTH // 2,
                            game_parameters.HEIGHT // 2 - 2),
                           Node((game_parameters.WIDTH // 2,
                                 game_parameters.HEIGHT // 2 - 1),
                                self.__head))
        self.__more_to_extend = 0
        self.__length = 3

    def get_head_value(self):
        """This function returns the snake's head's coordinates"""
        return self.__head.get_value()

    def get_tail_value(self):
        """This function returns the snake's tail's coordinates"""
        return self.__tail.get_value()

    def move_forward(self, drc):
        """This function moves the snake one step in the given direction
        (drc) except the snake's tail"""
        new_width = self.__head.get_value()[0] + DIRECTIONS[drc][0]
        new_height = self.__head.get_value()[1] + DIRECTIONS[drc][1]
        self.__head = self.__head.set_next((new_width, new_height))
        self.__length += 1

    def remove_tail(self):
        """This function removes the snake's tail (one node from the end of
        the snake"""
        self.__tail = self.__tail.get_next()
        self.__length -= 1

    def get_cords(self):
        """This function returns all the current coordinates of the snake"""
        coordinates = []
        current = self.__tail
        while current is not None:
            coordinates.append(current.get_value())
            current = current.get_next()
        return coordinates

    def get_more_to_extend(self):
        """This function returns the number of nodes that the snake need to
        extend"""
        return self.__more_to_extend

    def extended(self):
        """This function decreases the more to extend of the snake"""
        self.__more_to_extend -= 1

    def ate_an_apple(self):
        """This function adds 3 to the more to extend of the snake"""
        self.__more_to_extend += 3

    def get_length(self):
        """This function returns the current length of the snake"""
        return self.__length
