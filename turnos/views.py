from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from turnos.models import Turno
from turnos.serializers import TurnoSerializer


# Create your views here.

class TurnosAPIListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        pacient = get_object_or_404(User, username=request.user.username)
        serializer = TurnoSerializer(pacient.appointments, many=True)
        return Response({'turnos': serializer.data}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(pacient=self.request.user)

    def post(self, request, format=None):
        serializer = TurnoSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer=serializer)
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)

        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TurnosDetailView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk, format=None):
        turno = get_object_or_404(Turno, pk=pk)
        serializer = TurnoSerializer(instance=turno)
        return Response({"turno": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        turno = get_object_or_404(Turno, pk=pk)
        serializer = TurnoSerializer(turno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"actualizado": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        turno = get_object_or_404(Turno, pk=pk)
        turno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
