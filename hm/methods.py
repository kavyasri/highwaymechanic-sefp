from haversine import haversine
from django.contrib.auth.models import User
from hm.models import UserProfile, Service
from django.core import serializers
from hm import templatenames

def distance_between(user, mechanic):
	return haversine(user, mechanic)


def retrieve_all_usernames():
	usernames = list()
	for user in User.objects.all():
		usernames.append(user.get_username())

	return usernames

def searchNearbyMechanics(user_location, max_threshold_dist):
	mechanics = UserProfile.objects.filter(is_mechanic=True)
	MECHANIC_QUERY_LIST = list()
	for mechanic in mechanics:		
			mechanic_latitude = mechanic.latitude 
			mechanic_longitude = mechanic.longitude
			
			mechanic_location = (mechanic_latitude, mechanic_longitude)
			distance = haversine( user_location, mechanic_location )
			if distance < max_threshold_dist:
				mechanic_object = dict()
				mechanic_object['distance'] = distance 
				mechanic_object['mechanic'] = mechanic.user.id
				mechanic_object['mobile'] = mechanic.mobile 
				mechanic_object['name'] = mechanic.user.get_full_name()
				MECHANIC_QUERY_LIST.append(mechanic_object)
	return MECHANIC_QUERY_LIST
def serialize_list(list_model):
	return serializers.serialize("xml", list_model)

def location_caliberate(location):
	if location == None:
		return templatenames.GARBAGE_LOCATION
	else:
		return location

