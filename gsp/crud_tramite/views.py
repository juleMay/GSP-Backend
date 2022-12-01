from .serializers import *
from .models import Tramite
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def tramite_list(request):
    """
    POST: Retorna la lista de elementos del modelo Tramites en formato Json.
    GET: Guarda nuevas entradas del modelo Tramites.
    """
    if request.method == 'GET':
        # Recupera todos los elementos de la BD
        tramites = Tramite.objects.all()
        # Serializa la lista a Json
        serializer = TramiteSerializer(tramites, many=True)
        return Response({"tramites": serializer.data})
    elif request.method == 'POST':
        # Crea un objeto de tipo Tramite apartir de los datos de la peticion
        serializer = TramiteSerializer(data=request.data)
        if serializer.is_valid:
            # Guarda el elemento validado en la BD
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


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
        if serializer.is_valid:
            # Guarde el Tramite modificado en la BD
            serializer.save
            return Response(serializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.methos == 'DELETE':
        # Elimina el Tramite con el id de la peticion de la BD
        tramite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
