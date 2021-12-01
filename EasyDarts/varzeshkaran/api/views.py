import json

from django.http import JsonResponse
from django.http.response import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from varzeshkaran.api.serializer import *
from varzeshkaran.models import *

@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def get_all_Athletes(request):
    if request.method == 'GET':
        all_players = Athlete.objects.all()
        serializer = PlayerSerializer(all_players, many=True)

        data = json.loads(json.dumps(serializer.data))
        return Response(data,status=status.HTTP_200_OK)
    else:
        myData = JSONParser().parse(request)
        ASerializer = PlayerSerializer(data=myData)
        if ASerializer.is_valid():
            return Response(ASerializer , status=status.HTTP_201_CREATED)
        return Response(ASerializer.errors , status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def Athlete_Profile(request,id = None):
    athlete = Athlete.objects.get(user_id = id)
    serializer = PlayerSerializer(athlete)
    data = json.loads(json.dumps(serializer.data))
    return Response(data,status=status.HTTP_200_OK)
  


@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def get_all_Refrees(request):
    if request.method == 'GET':
        all_refrees = Refree.objects.all()
        serializer = RefreeSerializer(all_refrees, many=True)

        data = json.loads(json.dumps((serializer.data)))
        return Response(data, status=status.HTTP_200_OK)
    else:
        myData = JSONParser().parse(request)
        RSerializer = RefreeSerializer(data=myData)

        if RSerializer.is_valid():
            RSerializer.save()
            return Response(RSerializer.data , status=status.HTTP_201_CREATED)
        return Response(RSerializer.errors , status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def Refree_Detail(request , id = None):
    refree = Refree.objects.get(user_id= id)
    serializer = RefreeSerializer(refree)
    data = json.loads(json.dumps(serializer.data))
    return Response(data,status=status.HTTP_200_OK)
  
    


@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def get_all_coaches(request):
    if request.method == 'GET':
        all_coaches = Coach.objects.all()
        serializer = CoachSerializer(all_coaches, many=True)

        data = json.loads(json.dumps(serializer.data))
        return Response(data, status=status.HTTP_200_OK)
    else:
        myData = JSONParser().parse(request)
        AdminClubSerializer = AdminSerializer(data=myData)

        if AdminClubSerializer.is_valid():
            AdminClubSerializer.save()
            return Response(AdminClubSerializer.data , status=status.HTTP_201_CREATED)

        return Response(AdminClubSerializer.errors , status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def Coach_Detail(request , id = None):
    coach = Coach.objects.get(user_id= id)
    serializer = CoachSerializer(coach)
    data = json.loads(json.dumps(serializer.data))
    return Response(data,status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def admin_list(request):
    if request.method == 'GET':
        all_admins = AdminOfClub.objects.all()
        mySerializer = AdminSerializer(all_admins , many=True)
        data = json.loads(json.dumps(mySerializer.data))
        return Response(data , status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        mySerializer = AdminSerializer(data=data)

        if mySerializer.is_valid():
            mySerializer.save()
            return Response(mySerializer.data,
                                status = status.HTTP_201_CREATED
                                )
        return Response(mySerializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

@permission_classes((IsAuthenticated))
@api_view(['GET'])
def AdminClub_Detail(request , id = None):
    admin = AdminOfClub.objects.get(user_id = id)
    serializer = AdminSerializer(admin)
    data = json.loads(json.dumps(serializer.data))
    return Response(data,status=status.HTTP_200_OK)



@permission_classes((IsAuthenticated))
@api_view(['GET' , 'POST'])
def race_list(request):
    if request.method == 'GET':
        all_Races = Race.objects.all()
        RaceSeri = RaceSerializer(all_Races , many=True)
        RaceData = json.loads(json.dumps(RaceSeri.data))
        return Response(RaceData , status=status.HTTP_200_OK)

    else:
        data = JSONParser().parse(request)
        RaSerializer = RaceSerializer(data=data)

        if RaSerializer.is_valid():
            RaSerializer.save()
            return Response(RaSerializer.data , status=status.HTTP_201_CREATED)

        return Response(RaSerializer.errors, status=status.HTTP_400_BAD_REQUEST)