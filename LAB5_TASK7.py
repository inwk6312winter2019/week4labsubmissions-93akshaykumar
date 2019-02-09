class Kangaroo:
	def __init__(self):
		self.pouch_contents=[]
	def put_in_pouch(self,obj):
		self.pouch_contents.append(obj)
	def __str__(self):
		return "The string object::"+str(self.pouch_contents)

kanga=Kangaroo()
roo=Kangaroo()
roo.pouch_contents.append('This is the roo object list')
kanga.put_in_pouch(roo)

for obj in kanga.pouch_contents:
	print('Printing Kanga obj list::',obj)

