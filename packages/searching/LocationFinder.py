import re

from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.gis.measure import Distance
from cities.models import City, Region, Country


class LocationFinder:
    MAX_CITY_RESULTS = 15

    def distanceSearch(self, city, miles=5):
        return City.objects.distance(city.location).exclude(id=city.id).filter(
            location_1_distance_lte=(city.location, Distance(mi=miles))).order_by('distance')[:self.MAX_CITY_RESULTS]

    def search(self, query, results=MAX_CITY_RESULTS):
        return City.objects.annotate(search=SearchVector('name', 'region__name', 'region__code')).filter(
            search=query).order_by('-population')[:results]

    def findCity(self, query):
        return self.search(query, 1)[0]