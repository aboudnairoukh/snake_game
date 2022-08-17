class Bomb:
    """This class represent the bombs in the game"""
    def __init__(self, coordinate, radius, time):
        self.__coordinate = coordinate
        self.__radius = radius
        self.__time = time
        self.__explosion = Explosion(self)

    def get_coordinate(self):
        """This function returns the bombs coordinate"""
        return self.__coordinate

    def update_time(self):
        """This function updates the bombs timer"""
        self.__time -= 1

    def exploded(self):
        """This function return True if the timer is 0 and False if not"""
        return self.__time == 0

    def get_radius(self):
        """This function returns the current radius of the bomb"""
        return self.__radius

    def update_radius(self):
        """This function decreases the radius of the bomb and extend the
        explosions radius"""
        self.__radius -= 1
        self.__explosion.extend_explosion_radius()

    def get_explosion_coordinates(self):
        """This function returns the current coordinates of the explosion"""
        return self.__explosion.get_coordinates(self)


class Explosion:
    """This class represents the explosion of the current bomb"""
    def __init__(self, bomb):
        self.__center_cord = bomb.get_coordinate()
        self.__exp_radius = 0

    def extend_explosion_radius(self):
        """This function extends the radius of the explosion"""
        self.__exp_radius += 1

    def diagonal(self):
        """This function calculates and returns the coordinates of the
         diagonal explosion pixels based on the radius"""
        coordinates = set()
        up = (self.__center_cord[0], self.__center_cord[1] + self.__exp_radius)
        down = (self.__center_cord[0], self.__center_cord[1] - self.__exp_radius)
        for i in range(self.__exp_radius + 1):
            coordinates.add((up[0] + i, up[1] - i))
            coordinates.add((up[0] - i, up[1] - i))
            coordinates.add((up[0] + i, down[1] + i))
            coordinates.add((up[0] - i, down[1] + i))
        return coordinates

    def get_coordinates(self, bomb):
        """This function returns all the coordinates of the explosion"""
        if self.__exp_radius == 0:
            return [self.__center_cord]
        coordinates = list(self.diagonal())
        return coordinates
