import math
class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __str__(self):
		return "The Points are ({},{})".format(self.x,self.y)

	def distance_between_points(self,other):
		return math.sqrt(((other.x-self.x)**2)-((other.y-self.y)**2)) 
	def __add__(self,other):
		return (self.x+other.x,self.y+other.y)
	
point1=Point(10,50)
point2=Point(40,60)
print(point1)
print('The Sum of the points is ::',point1+point2)
#point1.distance_between_points(point2)
#print('The distance between two points are::',point1.distance_between_points(point2))
