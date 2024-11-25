'''
Activity 3, Group 6
Students: Shaikha Alhajri, Fatma Alsuwaidi, Fatma Almadani, Iliazya Alattar, Noha Abou Karnib
This activity is to help guide us on how TDD can help when creating a class to ensure all the values are outputed as expected!
'''
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
    
    ''' Defult sides for the triangle, square, and hexagon shapes '''
    def instantiate_polygon(self):
        if self.get_name().lower() == 'triangle':
            self.set_sides([3,3,3])
            return f'{self.__str__()}, {str(self.calculate_circumference())}'
        elif self.get_name().lower() == 'square':
            self.set_sides([4,4,4,4])
            return f'{self.__str__()}, {str(self.calculate_circumference())}'
        elif self.get_name().lower() == 'hexagon':
            self.set_sides([6,6,6,6,6,6])
            return f'{self.__str__()}, {str(self.calculate_circumference())}'
        
# Executing the main function      
if __name__ == '__main__':
    p1 = Polygon('Triangle', [])
    p2 = Polygon('Square', [])
    p3 = Polygon('Hexagon', [])
    print(p1.instantiate_polygon())
    print(p2.instantiate_polygon())
    print(p3.instantiate_polygon())
    print(p1 == p2)  # False
    print(p1 != p3)  # True
    
    