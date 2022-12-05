from .serializers import ConfiguracionSerializer
from .models import Configuracion
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def traslado_list(request):
    """
    GET: Guarda nuevas entradas del modelo Configuraciones.
    """
    if request.method == 'GET':
        # Recupera todos los elementos de la BD
        configuraciones = Configuracion.objects.all()
        # Serializa la lista a Json
        serializer = ConfiguracionSerializer(configuraciones, many=True)
        return Response({"configuraciones": serializer.data})
    elif request.method == 'POST':
        # Crea un objeto de tipo Configuracion apartir de los datos de la peticion
        serializer = ConfiguracionSerializer(data=request.data)
        if serializer.is_valid():
            # Guarda el elemento validado en la BD
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def traslado_detail(request, id):
    """
    GET: Retorna un individuo del modelo Configuraciones en formato Json con pk = id.
    PUT: Modifica un individuo del modelo Configuraciones con pk = id.
    """
    try:
        # Intenta buscar el Configuracion con el id de la peticion
        configuracion = Configuracion.objects.get(pk=id)
    except Configuracion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serializa el elemento de Configuracion en formato Json
        serializer = ConfiguracionSerializer(configuracion)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Modifica el Configuracion a partir de los datos de la peticion
        serializer = ConfiguracionSerializer(configuracion, data=request.data)
        if serializer.is_valid():
            # Guarde el Configuracion modificado en la BD
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)