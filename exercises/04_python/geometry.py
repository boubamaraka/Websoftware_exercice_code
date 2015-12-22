import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance_from(self,addr):
        val=pow((addr.x-self.x),2)
        val2=pow((addr.y-self.y),2)
        dis=val+val2
        return (math.sqrt(dis))

#p2.distance_from()
class Circle(Point):
    def __init__(self,center,radius):
        self.center=center
        self.radius=radius
    def is_inside(self,addr):
        if pow((addr.x - self.center.x), 2) + pow((addr.y - self.center.y), 2) < pow(self.radius, 2):
            return True
        else:
            return False
p1=Point(0,0)
p2 = Point(2,4)
print(p1.distance_from(p2))
circle = Circle(p2,4)
print(circle.is_inside(p1))
print(circle.is_inside(Point(2,2)))
