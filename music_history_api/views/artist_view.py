from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class ArtistViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow artists to be viewed or edited
	@rtwhitfield84

	"""

	def get_queryset(self):

		"""
		overides the default method to dynamically determine queryset
		returns the artists associated with the current user

		"""

		if self.request.user.is_superuser:
			return artist_model.Artist.objects.all()
		else:
			return artist_model.Artist.objects.filter(user=self.request.user)

	serializer_class = artist_serializer.ArtistSerializer