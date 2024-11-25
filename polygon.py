class Polygon:
    __slots__ = ['__name','__sides'] # Makes sure that the Polygon class ONLY has these two members
    ''' Initilize with 2 private members, name and sides '''
    def __init__(self, name, sides):
        self.__name = name
        self.__sides = sides
    
    ''' Getting and setting the name of the polygon '''
    def get_name(self):
        return self.__name
    def set_name(self, new_value):
        self.__name = new_value
    ''' Getting and setting the number of sides of the polygon '''
    def get_sides(self):
        return self.__sides
    def set_sides(self, new_value):
        self.__sides = new_value
    
    ''' Checking the inequality of the polygon '''
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__name == other.get_name() and self.__sides == other.get_sides()
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)

    ''' Creating a string representation of a polygon object '''
    def __str__(self):
        return self.__name + " with sides: " + str(self.__sides)

    ''' Calculating the sum of all sides of the polygon '''
    def calculate_circumference(self):
        return sum(self.__sides)
    