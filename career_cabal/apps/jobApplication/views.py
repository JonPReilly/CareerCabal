from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
