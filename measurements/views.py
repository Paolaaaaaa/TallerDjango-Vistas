from .logic import measurements_logic as ms
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = ms.get_measurment(id)
            measurement = serializers.serialize('json',[measurement_dto])
            return HttpResponse(measurement,'application/json')
        else:
            measurement_dto = ms.get_measurements()
            measurement = serializers.serialize('json',measurement_dto)
            return HttpResponse(measurement, 'application/json')
    if request.method == 'POST':
        measurement_dto=ms.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json',[measurement_dto])
        return HttpResponse(measurement,'application/json')



@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = ms.get_measurment(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement,'application/json')
    if request.method == 'PUT':
        measurment_dto= ms.update_measurements(pk, json.loads(request.body))
        measurement = serializers.serialize('json',[measurment_dto,])
        return HttpResponse(measurement,'application/son')
    if request.method =='DELETE':
        measurement_dto = ms.delete_measurments(pk)
        measurement = serializers.serialize('json',[measurement_dto,])
        return HttpResponse(measurement, 'application/json')