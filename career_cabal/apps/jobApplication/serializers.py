from rest_framework import serializers

from apps.job.serializers import JobSerializer
from apps.user.serializers import UserSerializer

from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = JobApplication
        fields = '__all__'

