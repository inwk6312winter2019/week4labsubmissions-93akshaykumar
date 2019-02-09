class time:
	def __init__(self,seconds):
		self.allsecs=seconds
		self.minutes,self.seconds=divmod(seconds,60)
		self.hours,self.minutes=divmod(self.minutes,60)

	def __str__(self):
		return ('Time is :: %.2d:%.2d:%.2d')%(self.hours,self.minutes,self.seconds)
	def is_after(self,other):
		return other.allsecs > self.allsecs
t1=time(1234567890)
t2=time(2345678987)
print(t1)
print(t2)
print('Does The Time follows time cronologically::',t2.is_after(t1))
