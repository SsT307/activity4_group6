from polygon import Polygon

def test_polygon_initialization():
    polygon = Polygon("Triangle", [3, 3, 3])  
    assert polygon.get_name() == "Triangle" 
    assert polygon.get_sides() == [3, 3, 3] 

def test_set_sides():
    polygon = Polygon("Square", [4, 4, 4, 4])
    polygon.set_sides([5, 5, 5, 5])  
    assert polygon.get_sides() == [5, 5, 5, 5]
    
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