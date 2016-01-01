from haversine import haversine

def distance_between(user, mechanic):
	return haversine(user, mechanic)

