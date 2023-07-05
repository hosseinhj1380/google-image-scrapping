from django.shortcuts import render
from .models import scrap_request
# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import  AllowAny
from rest_framework.response import Response 
from rest_framework import status 

class Scrapping_request(CreateAPIView):
    permission_classes = [AllowAny,]

    def post (self,request):
        data=request.data
        obj=scrap_request(title=data['title'],quantity=data['quantity'])    
        obj.save()
        return Response({"message":"saved successfuly !"},status.HTTP_200_OK)

    
