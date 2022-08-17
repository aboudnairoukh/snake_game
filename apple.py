class Apple:
    """This class represent an apple in the game"""

    def __init__(self, coordinate, score):
        self.__coordinate = coordinate
        self.__score = score

    def get_coordinate(self):
        """This function returns the coordinate of the apple"""
        return self.__coordinate

    def get_score(self):
        """This function returns the score of the apple"""
        return self.__score
