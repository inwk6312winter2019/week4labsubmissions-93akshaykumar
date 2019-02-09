class Vehicle:
	pass
class LandVehicle(Vehicle):
	pass
class TrackedVehicle(LandVehicle):
	pass

vehicle = Vehicle()
landvehicle = LandVehicle()
trackedvehicle = TrackedVehicle()

for ob in [vehicle, landvehicle, trackedvehicle]:
	for cl in [Vehicle, LandVehicle, TrackedVehicle]:
		print(str(ob.__class__.__name__)+' is the instance of '+str(cl.__name__)+' ::)',isinstance(ob,cl))

