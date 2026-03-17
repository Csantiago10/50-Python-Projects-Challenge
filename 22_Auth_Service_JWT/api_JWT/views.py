from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ComputerSerializer
from .models import Computer


# Create your views here.

# Get and create data in database
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def computer_list(request):
    if request.method == 'GET':
        computers = Computer.objects.all()
        serializer = ComputerSerializer(computers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ComputerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get, update and delete data in database
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def computer_detail(request, pk):
    try:
        computer = Computer.objects.get(pk=pk)
    except Computer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ComputerSerializer(computer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ComputerSerializer(computer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        computer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)