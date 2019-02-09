class time:
	def __init__(self,seconds):
		self.minutes,self.seconds=divmod(seconds,60)
		self.hours,self.minutes=divmod(self.minutes,60)
		print(self.hours,self.minutes,self.seconds)

	def __str__(self):
		return ('Time is :: %.2d:%.2d:%.2d')%(self.hours,self.minutes,self.seconds)
t1=time(1234567890)

print(t1)
