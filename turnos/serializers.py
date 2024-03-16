from rest_framework.serializers import ModelSerializer
from turnos.models import Turno

class TurnoSerializer(ModelSerializer):
    class Meta:
        model = Turno
        fields = ['id', 'title', 'description', 'date']
