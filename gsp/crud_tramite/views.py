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
        tramites = Tramite.objects.all()
        serializer = TramtiteSerializer(tramites, many=True)
        return Response({"tramites": serializer.data}, status=status.HTTP_200_OK)
    
@api_view(['GET', 'PUT', 'DELETE'])
def tramite_detail(request, id):
    """
    GET: Retorna un individuo del modelo Tramites en formato Json con pk = id.
    PUT: Modifica un individuo del modelo Tramites con pk = id.
    DELETE: Elimina un individuo del modelo Tramites con pk = id.
    """
    try:
        tramite = Tramite.objects.get(pk=id)
    except Tramite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TramtiteSerializer(tramite)
        return Response(serializer.data)