import math
class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def distance_between_points(self,other):
		return math.sqrt(((other.x-self.x)**2)-((other.y-self.y)**2)) 

point1=Point(10,50)
point2=Point(40,60)
#point1.distance_between_points(point2)
print('The distance between two points are::',point1.distance_between_points(point2))
