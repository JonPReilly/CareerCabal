from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.jobApplication.models import JobApplication
from apps.jobApplication.serializers import JobApplicationSerializer

class JobBoard(APIView):
    def get(self,request,format=None):
        lanes = {
                    'main' : [
                                {'id' : 8, 'description' : 'Saved'},
                                {'id' : 1, 'description' : 'Applied'},
                                {'id' : 2, 'description' : 'Coding Challange'},
                                {'id' : 7, 'description' : 'Phone Interview'},
                                {'id' : 6, 'description' : 'Onsite Interview'},
                                {'id' : 5, 'description' : 'Offer'},
                             ]
                }
        return Response(lanes, status.HTTP_200_OK)


class JobApplicationView(APIView):

    def get(self,request,format=None):
        if not request.user.is_authenticated:
            return Response({'status': 'Unauthorized'},status.HTTP_401_UNAUTHORIZED)

        user = request.user
        applications = JobApplication.objects.filter(user=user)
        serialized_applications = JobApplicationSerializer(applications,many=True)
        return Response({
            'user_id' : user.pk,
            'status' : 'Ok',
            'count' :applications.count() ,
            'applications' : serialized_applications.data
            }, status.HTTP_200_OK)
