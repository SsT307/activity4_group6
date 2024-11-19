class Polygon:
    __slots__ = ['__name','__sides']
    def __init__(self, name, sides):
        self.__name = name
        self.__sides = sides
    
    def get_name(self):
        return self.__name
    def set_name(self, new_value):
        self.__name = new_value
    
    def get_sides(self):
        return self.__sides
    def set_sides(self, new_value):
        self.__sides = new_value
