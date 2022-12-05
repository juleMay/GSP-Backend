from .serializers import TrasladoSerializer
from crud_tramite.models import Traslado
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def traslado_list(request):
    """
    POST: Retorna la lista de elementos del modelo Traslados en formato Json.
    GET: Guarda nuevas entradas del modelo Traslados.
    """
    if request.method == 'GET':
        # Recupera todos los elementos de la BD
        traslados = Traslado.objects.all()
        # Serializa la lista a Json
        serializer = TrasladoSerializer(traslados, many=True)
        return Response({"traslados": serializer.data})
    elif request.method == 'POST':
        # Crea un objeto de tipo Traslado apartir de los datos de la peticion
        serializer = TrasladoSerializer(data=request.data)
        if serializer.is_valid():
            # Guarda el elemento validado en la BD
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def traslado_detail(request, id):
    """
    GET: Retorna un individuo del modelo Traslados en formato Json con pk = id.
    PUT: Modifica un individuo del modelo Traslados con pk = id.
    DELETE: Elimina un individuo del modelo Traslados con pk = id.
    """
    try:
        # Intenta buscar el Traslado con el id de la peticion
        traslado = Traslado.objects.get(pk=id)
    except Traslado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serializa el elemento de Traslado en formato Json
        serializer = TrasladoSerializer(traslado)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Modifica el Traslado a partir de los datos de la peticion
        serializer = TrasladoSerializer(traslado, data=request.data)
        if serializer.is_valid():
            # Guarde el Traslado modificado en la BD
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Elimina el Traslado con el id de la peticion de la BD
        traslado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
