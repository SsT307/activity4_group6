from polygon import Polygon

'''
Test for negative
Zeroes
test setters

'''

''' 
*           *           *           *           *           *
Activity 4: In this assignment we are combining our knowledge from the previous lesson of test
driven development (TDD), where we are checking if our class functions are working as intended.
We created a class called Polygon, where we created many constructors to get and set the states
of an object, constructors to check if two objects are the same or not, and, finally, a construtor
to caculate the circumference/perimeter, which just adds all the sides together.
*           *           *           *           *           *
'''
# --------------------------------------------------------------------------------------- #
''' *           *           *     STEP 1      *           *           * '''
'''
In this step we are asked to test the getter and setter methods. We checked that the function of 
get_name() fetchesthe name of the polygon and that the setter function is able to mutate the objects 
state, and whatever the output is will be checked with the assert function. This will ensure that 
the given output is exactly as expected.
We also would like to check that the polygon is, well, a polygon! We need to first check that the 
polygon actually has sides and that it is not equal to zero, then we need to check if the sides are 
postive numbers 
'''

def test_polygon_initialization():
    ''' Test that the polygon has sides and that it is not equal to zero '''
    polygon1 = Polygon('Nonagon', [5,7,8])
    assert sum(polygon1.get_sides()) != 0 # Will return True, because the total of the variables in the list does not equal to zero
    # Test that the sides are positive numbers
    polygon2 = Polygon('Shape', [1, 2, 3, 4, 5])
    assert all(polygon2.get_sides() > 0 for polygon2.get_sides() in polygon2.sides) # Will return True, because the sum of the

def test_get_sides():
    ''' Test that the get_sides() method returns the correct list of sides '''
    polygon = Polygon("Triangle", [3, 3, 3])  
    assert polygon.get_name() == "Triangle" 
    assert polygon.get_sides() == [3, 3, 3] 

def test_set_sides():
    ''' Test that the set_sides() method sets the sides correctly '''
    polygon = Polygon("Square", [4, 4, 4, 4])
    polygon.set_sides([5, 5, 5, 5])  # Changes the list of sides ([4, 4, 4, 4] --> [5, 5, 5, 5])
    assert polygon.get_sides() == [5, 5, 5, 5]

# --------------------------------------------------------------------------------------- #

''' *           *           *     STEP 2      *           *           * '''
def test_polygon_equality():
    ''' Test that the __eq__ method work correctly '''
    polygon1 = Polygon("Triangle", [3, 3, 3])
    polygon2 = Polygon("Triangle", [3, 3, 3])
    assert polygon1.__eq__(polygon2) # Will return True because they ARE equal

def test_polygon_inequality():
    ''' Test that the __ne__ method work correctly '''
    polygon3 = Polygon("Triangle", [3, 3, 3])
    polygon4 = Polygon("Square", [3, 3, 3, 3])
    assert polygon3.__ne__(polygon4) # Will return True because they are NOT equal


# --------------------------------------------------------------------------------------- #

''' *           *           *     STEP 3      *           *           * '''
def test_polygon_str():
    ''' Test that the __str__ method returns a string representation of the polygon '''
    polygon = Polygon("Triangle", [3, 3, 3])  
    assert str(polygon) == "Triangle with sides: [3, 3, 3]"

def test_calculate_circumference():
    ''' Test that the calculate_circumference method returns the sum of all sides of the polygon '''
    s1 = Polygon("Square", [4, 4, 4, 4])
    assert s1.calculate_circumference() == 16 # 4 + 4 + 4 + 4 = 16
