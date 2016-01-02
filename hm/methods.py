from haversine import haversine
from django.contrib.auth.models import User

def distance_between(user, mechanic):
	return haversine(user, mechanic)


def retrieve_all_usernames():
	usernames = list()
	for user in User.objects.all():
		usernames.append(user.get_username())

	return usernames

