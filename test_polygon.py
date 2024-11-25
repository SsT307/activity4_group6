from polygon import Polygon
''' 
*           *           *           *           *           *
Activity 4: In this assignment we are combining our knowledge from the previous lesson of test
driven development (TDD), where we are checking if our class functions are working as intended.
We created a class called Polygon, where we created many constructors to get and set the states
of an object, constructors to check if two objects are the same or not, and, finally, a construtor
to caculate the circumference/perimeter, which just adds all the sides together.
*           *           *           *           *           *
'''
""" * * * * * * * * * STEP 1 * * * * * * * * * """
""" In this step we are asked to test the getter and setter methods. We checked that the function of 
get_name() fetchesthe name of the polygon and that the setter function is able to mutate the objects 
state, and whatever the output is will be checked with the assert function. This will ensure that 
the given output is exactly as expected.
We also would like to check that the polygon is, well, a polygon! We need to first check that the 
polygon actually has sides and that it is not equal to zero, then we need to check if the sides are 
postive numbers """

def test_polygon_initialization():
    # Test that the polygon has sides and that it is not equal to zero
    polygon1 = Polygon('Nonagon', [])
    assert len(polygon1.get_sides()) != 0
    # Test that the sides are positive numbers
    polygon2 = Polygon('Shape', [1, 2, 3, 4, 5])
    assert all(polygon2.get_sides() > 0 for polygon2.get_sides() in polygon2.sides)

def test_get_sides():
    polygon = Polygon("Triangle", [3, 3, 3])  
    assert polygon.get_name() == "Triangle" 
    assert polygon.get_sides() == [3, 3, 3] 

def test_set_sides():
    polygon = Polygon("Square", [4, 4, 4, 4])
    polygon.set_sides([5, 5, 5, 5])  
    assert polygon.get_sides() == [5, 5, 5, 5]

""" * * * * * * * * * STEP 2 * * * * * * * * * """
def __eq__(self, other):
        if type(self) == type(other):
            return self.__name == other.get_name() and self.__sides == other.get_sides()
        else:
            return False

def __ne__(self, other):
        return not self.__eq__(other)

def test_polygon_equality():
    polygon1 = Polygon("Triangle", [3, 3, 3])
    polygon2 = Polygon("Triangle", [3, 3, 3])
    assert polygon1.__eq__(polygon2) #will return True bcs they are equal

def test_polygon_inequality():
    polygon3 = Polygon("Triangle", [3, 3, 3])
    polygon4 = Polygon("Square", [3, 3, 3, 3])
    assert polygon3.__ne__(polygon4) #will return True bcs they are not equal

""" * * * * * * * * * STEP 3 * * * * * * * * * """
def test_polygon_str():
    polygon = Polygon("Triangle", [3, 3, 3])  
    assert str(polygon) == "Triangle with sides: [3, 3, 3]"

def test_calc_circumference():
    s1 = Polygon("Square", [4, 4, 4, 4])
    assert s1.calculate_circumference() == 16
