import math
class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def distance_between_points(self,other):
		return math.sqrt(((other.x-self.x)**2)-((other.y-self.y)**2)) 

class Rectangle(Point):
	def __init__(self,width=0,height=0,corner=(0,0)):
		self.width=width
		self.height=height
		self.corner=Point(corner[0],corner[1])

	def __str__(self):
		return 'WIDTH::'+str(self.width)+' HEIGHT::'+str(self.height)+' CORNER X::'+str(self.corner.x)+' Y::'+str(self.corner.y)


	def all_corner(self):
		corner1=(self.corner.x,self.corner.y)
		cornerx=(self.corner.x+self.height,self.corner.y)
		cornery=(self.corner.x,self.corner.y+self.width)
		corner2=(cornerx[0],cornerx[1]+self.width)
		return (corner1,cornerx,cornery,corner2)

	def calculate_center(self):
		corners=self.all_corner()
		cornerx=corners[1]
		cornery=corners[2]
		return ((cornerx[0]+cornery[0])/2,(cornerx[1]+cornery[1])/2)

	def shift_rectangle(self,dx,dy):
		corners=self.all_corner()
		cornerlist=[]
		for c in corners:
			cornerlist.append((c[0]+dx,c[1]+dy))
		return cornerlist

rec=Rectangle(10,20,(10,20))
rec2=rec

print('The Coordinates the rectangle are ::',rec.all_corner())

print('The Center Of the rectangle is ::',rec.calculate_center())


print('The Modified Cordinates Of the rectangle is ::',rec.shift_rectangle(10,10))


print('The Moved Cordinates Of the rectangle is ::',rec2.shift_rectangle(20,20))
