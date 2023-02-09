from .serializers import *
from .models import Tramite
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date, timedelta
from api_configuracion.models import Configuracion
from django.db.models import F
import math

def get_vencimiento (tipo_tramite, fecha_inicial):
    configuracion = Configuracion.objects.get(tipo_configuracion=tipo_tramite)
    dias_por_sumar = configuracion.tiempo_limite
    fecha_actual = fecha_inicial
    while dias_por_sumar > 0:
        fecha_actual += timedelta(days=1)
        dia_actual = fecha_actual.weekday()
        if dia_actual >= 5:
            continue
        dias_por_sumar -= 1
    return fecha_actual

def filter_tramites(filtro):
    fecha_actual = date.today()
    tramites=[]
    if (filtro == 'en-proceso'):
        tramites = Tramite.objects.exclude(fecha_vencimiento__lte=fecha_actual).exclude(fecha_vencimiento__lte=fecha_actual+timedelta(days=5))        
    elif(filtro == 'cerca-a-vencer'):
        tramites = Tramite.objects.exclude(fecha_vencimiento__lte=fecha_actual).filter(fecha_vencimiento__lte=fecha_actual+timedelta(days=5))
    elif(filtro == 'vencidos'):
        tramites = Tramite.objects.filter(fecha_vencimiento__lte=fecha_actual)
    return tramites

    

@api_view(['GET', 'POST'])
def tramite_list(request, filtro):
    """
    POST: Retorna la lista de elementos del modelo Tramites en formato Json.
    GET: Guarda nuevas entradas del modelo Tramites.
    """
    if request.method == 'GET':
        # Recupera todos los elementos de la BD
        if (filtro!="todos"):
            tramites = filter_tramites(filtro)
        else:
            tramites = Tramite.objects.all()
        # Serializa la lista a Json
        serializer = TramiteSerializer(tramites, many=True)
        
        return Response({"tramites": serializer.data})
    elif request.method == 'POST':
        # Crea un objeto de tipo Tramite apartir de los datos de la peticion
        serializer = TramiteSerializer(data=request.data)
        if serializer.is_valid():
            tipo_tramite = serializer.validated_data['tipo_tramite']
            fecha_inicial = serializer.validated_data['fecha_recepcion']
            serializer.validated_data['fecha_vencimiento'] = get_vencimiento(tipo_tramite,fecha_inicial)
            # Guarda el elemento validado en la BD
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_409_CONFLICT)

@api_view(['GET', 'PUT', 'DELETE'])
def tramite_detail(request, id):
    """
    GET: Retorna un individuo del modelo Tramites en formato Json con pk = id.
    PUT: Modifica un individuo del modelo Tramites con pk = id.
    DELETE: Elimina un individuo del modelo Tramites con pk = id.
    """
    try:
        # Intenta buscar el Tramite con el id de la peticion
        tramite = Tramite.objects.get(pk=id)
    except Tramite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serializa el elemento de Tramite en formato Json
        serializer = TramiteSerializer(tramite)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Modifica el Tramite a partir de los datos de la peticion
        serializer = TramiteSerializer(tramite, data=request.data)
        if serializer.is_valid():
            # Guarde el Tramite modificado en la BD
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Elimina el Tramite con el id de la peticion de la BD
        tramite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
