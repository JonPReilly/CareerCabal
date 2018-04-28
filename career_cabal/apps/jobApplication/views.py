from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class JobBoard(APIView):
    def get(self,request,format=None):
        lanes = {
                    8 : 'Saved',
                    1 : 'Applied',
                    2 : 'Coding Challange',
                    7 : 'Phone Interview',
                    6 : 'Onsite Interview',
                    5 : 'Offer'
                }
        return Response(lanes, status.HTTP_200_OK)
