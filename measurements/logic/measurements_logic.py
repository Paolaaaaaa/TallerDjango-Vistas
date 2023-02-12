from ..models import Measurement
from datetime import datetime
from  variables.logic import variables_logic as vl
from variables.models import Variable
#Get all measurements
def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

#Get mesurement pk
def get_measurment(pk_):
    measurement = Measurement.objects.get(pk=pk_)
    return measurement

def update_measurements(ms_pk, new_ms_val):
    measurement = get_measurment(ms_pk)
    
    measurement.value = new_ms_val["value"]
    measurement.unit = new_ms_val["unit"]
    measurement.place = new_ms_val["place"]
    measurement.dateTime = datetime.now()
    measurement.variable = Variable.objects.get(pk = new_ms_val["variable"][0])
    measurement.save()
    return measurement
def create_measurement(mesur):
    measurement = Measurement(
    value = mesur["value"], 
    unit= mesur["unit"], 
    place=mesur["place"],
    variable= Variable.objects.get(pk=mesur["variable"][0]))
    
   
    measurement.save()
    return measurement

def delete_measurments(var):
    measurement = get_measurment(var)
    measurement.delete()
    return measurement
    
