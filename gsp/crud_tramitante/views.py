from .serializers import TramitanteSerializer
from crud_tramite.models import Tramitante
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def tramitante_list(request):
    """
    POST: Retorna la lista de elementos del modelo Tramitante en formato Json.
    GET: Guarda nuevas entradas del modelo Tramitante.
    """
    if request.method == 'GET':
        # Recupera todos los elementos de la BD
        tramitantes = Tramitante.objects.all()
        # Serializa la lista a Json
        serializer = TramitanteSerializer(tramitantes, many=True)
        return Response({"tramitantes": serializer.data})
    elif request.method == 'POST':
        # Crea un objeto de tipo Tramitante apartir de los datos de la peticion
        serializer = TramitanteSerializer(data=request.data)
        if serializer.is_valid():
            # Guarda el elemento validado en la BD
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def tramitante_detail(request, id):
    """
    GET: Retorna un individuo del modelo Tramitantes en formato Json con pk = id.
    PUT: Modifica un individuo del modelo Tramitantes con pk = id.
    DELETE: Elimina un individuo del modelo Tramitantes con pk = id.
    """
    try:
        # Intenta buscar el Tramitante con el id de la peticion
        tramitante = Tramitante.objects.get(pk=id)
    except Tramitante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serializa el elemento de Tramitante en formato Json
        serializer = TramitanteSerializer(tramitante)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Modifica el Tramitante a partir de los datos de la peticion
        serializer = TramitanteSerializer(tramitante, data=request.data)
        if serializer.is_valid():
            # Guarde el Tramitante modificado en la BD
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Elimina el Tramitante con el id de la peticion de la BD
        tramitante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
