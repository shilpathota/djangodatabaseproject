from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import DatabaseapiCacdata
from .serializers import CACDataSerializers

# Create your views here.
class CACDataList(APIView):
    def get(self, request):
        ticketId1 = DatabaseapiCacdata.objects.all()
        serializer = CACDataSerializers(ticketId1, many=True)
        return Response(serializer.data)
        pass
    def post(self, request):
        pass