from rest_framework import serializers

from cities.models import City, Region, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id' , 'name')


class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = Region
        fields = ('id', 'name','country')

class CitySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    class Meta:
        model = City
        fields = ('id', 'name', 'region')
