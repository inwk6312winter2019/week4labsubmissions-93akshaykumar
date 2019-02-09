class Vehicle:
	pass
class LandVehicle(Vehicle):
	pass
class TrackedVehicle(LandVehicle):
	pass
for cl1 in [Vehicle, LandVehicle, TrackedVehicle]:
	for cl2 in [Vehicle, LandVehicle, TrackedVehicle]:
		print(str(cl1.__name__)+'is subclass of '+str(cl2.__name__)+' - ::)',issubclass(cl1,cl2))
	print()

