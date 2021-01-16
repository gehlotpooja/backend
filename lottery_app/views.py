from django.shortcuts import render
from .configuration import *
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def lobby_creation_api(request):
    data = {
        'msg':'Entry lobby details',
        'success':False
    }
    try:
        data = lobby_creation(request)
    except Exception as e:
        print(e.args)
    return Response(data=data,status=status.HTTP_200_OK)


@api_view(['POST'])
def adding_member_api(request):
    data = {
        'msg':'Enter member details',
        'success':False
    }
    try:
        data = adding_member(request)
    except Exception as e:
        print(e.args)
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET'])
def check_winner_api(request):
    data = {
        'msg':'Enter lobby id/name',
        'success':False
    }
    try:
        data = check_winner(request)
    except Exception as e:
        print(e.args)
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET'])
def dashboard_api(request):
    data = {
        'msg':'No data available',
        'success':False
    }
    try:
        data = dashboard(request)
    except Exception as e:
        print(e.args)
    return Response(data= data, status=status.HTTP_200_OK)