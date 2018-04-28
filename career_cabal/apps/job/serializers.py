from rest_framework import serializers

from apps.cities.serializers import CitySerializer
from apps.company.serializers import CompanySerializer

from .models import Job

class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    city = CitySerializer(read_only=True)
    class Meta:
        model = Job
        fields = '__all__'

