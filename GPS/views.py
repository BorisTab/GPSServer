from django.shortcuts import render
from .models import Coordinates
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def coordinates(request):
    if request.method == 'GET':
        coor = Coordinates.objects.first()
        lon = coor.lon
        lat = coor.lat
        data = {'lat': lat, 'lon': lon}
        response = JsonResponse(data)
        return response
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        lat = data['lat']
        lon = data['lon']
        coor = Coordinates.objects.first()
        coor.lon = lon
        coor.lat = lat
        coor.save()

        response = JsonResponse({"status": "Ok"})
        return response
